from collections import defaultdict

import polars as pl


# Mapping for model and score display names
MODEL = ["baseline", "site_only", "all_phenotypes"]
MODEL = {model: " ".join(model.split("_")).title() for model in MODEL}

SCORE = ["accuracy", "precision", "recall", "f1"]
SCORE = {score: score.title() for score in SCORE}
SCORE["roc_auc"] = "AUROC"
SCORE["matthews_corrcoef"] = "MCC"


def compile_results(cv_results, sort_by):
    """
    Compile and summarize cross-validation results into a formatted Polars DataFrame.

    Parameters
    ----------
    cv_results : dict of str -> pl.DataFrame or dict of str -> dict of str -> list
        Dictionary mapping model names to cross-validation results.
        Each entry should either be a Polars DataFrame or a dictionary of dictionary of list.
    sort_by : str
        Metric to use for selecting the best-performing model variant.
        Available ones include: "accuracy", "precision", "recall", "f1", "roc_auc",
        and "matthews_corrcoef".

    Returns
    -------
    compiled_results : pl.DataFrame
        Summary table with models as rows and formatted score strings (mean ± std) as columns.
    """
    compiled_results = defaultdict(list)

    for model in cv_results:
        # Ensure results are in Polars DataFrame format
        if not isinstance(cv_results[model], pl.DataFrame):
            cv_results[model] = pl.DataFrame(cv_results[model])

        df = cv_results[model]

        # Extract all available test scores
        scores = [
            col.removeprefix("rank_test_")
            for col in df.columns
            if col.startswith("rank_test_")
        ]

        # Sort and select best row based on rank of the chosen metric
        sort_col = f"rank_test_{sort_by}"
        best_row = df.sort(sort_col).row(0)  # get first row as tuple

        columns = df.columns
        row_dict = dict(zip(columns, best_row))

        compiled_results["Model"].append(MODEL[model])

        for score in scores:
            mean_score = row_dict[f"mean_test_{score}"]
            std_score = row_dict[f"std_test_{score}"]
            compiled_results[SCORE[score]].append(f"{mean_score:.4f} ± {std_score:.4f}")

    # Convert to Polars DataFrame and index by model
    compiled_results = pl.DataFrame(compiled_results)
    compiled_results = compiled_results.sort("Model")

    return compiled_results
