import pandas as pd
from collections import defaultdict
from sklearn.utils._param_validation import validate_params, StrOptions

__all__ = ["compile_results"]

# Mapping for model and score display names
MODEL = ["baseline", "site_only", "all_phenotypes"]
MODEL = {model: " ".join(model.split("_")).title() for model in MODEL}

SCORE = ["accuracy", "precision", "recall", "f1"]
SCORE = {score: score.title() for score in SCORE}
SCORE["roc_auc"] = "AUROC"
SCORE["matthews_corrcoef"] = "MCC"


@validate_params(
    {"cv_results": [dict], "sort_by": [StrOptions(set(SCORE))]},
    prefer_skip_nested_validation=True,
)
def compile_results(cv_results, sort_by):
    """
    Compile and summarize cross-validation results into a formatted DataFrame.

    Parameters
    ----------
    cv_results : dict of str -> pd.DataFrame or dict of str -> dict of str -> list
        Dictionary mapping model names to cross-validation results.
        Each entry should either be a DataFrame or a dictionary of dictionary of list.

    sort_by : str
        Metric to use for selecting the best-performing model variant.
        Available ones include: "accuracy", "precision", "recall", "f1", "roc_auc",
        and "matthews_corrcoef".

    Returns
    -------
    compiled_results : pd.DataFrame
        Summary table with models as rows and formatted score strings (mean ± std) as columns.
    """
    compiled_results = defaultdict(list)

    for model in cv_results:
        # Ensure results are in DataFrame format
        if not isinstance(cv_results[model], pd.DataFrame):
            cv_results[model] = pd.DataFrame(cv_results[model])

        # Extract all available test scores
        scores = [
            score.replace("rank_test_", "")
            for score in cv_results[model].columns
            if "rank_test" in score
        ]

        # Select the best row (lowest rank) based on the given metric
        cv_result = cv_results[model].sort_values(f"rank_test_{sort_by}").iloc[0]

        compiled_results["Model"].append(MODEL[model])

        for score in scores:
            mean_score = cv_result[f"mean_test_{score}"]
            std_score = cv_result[f"std_test_{score}"]
            compiled_results[SCORE[score]].append(f"{mean_score:.4f} ± {std_score:.4f}")

    # Convert to DataFrame and index by model name
    compiled_results = pd.DataFrame(compiled_results)
    compiled_results = compiled_results.set_index("Model")

    return compiled_results


@validate_params(
    {"param_grid": [list, None], "exclude": [str, None]},
    prefer_skip_nested_validation=True,
)
def parse_param_grid(param_grid=None, exclude=None):
    """
    Parse and filter the parameter grid to exclude specific parameters.

    Parameters
    ----------
    param_grid : list of key-value pairs or None
        List of key-value pairs representing the parameter grid for hyperparameter tuning.

    exclude : str or None
        Parameter name to exclude from the grid. If None, no parameters are excluded.

    Returns
    -------
    parsed_param_grid : dict or None
        Filtered parameter grid as a dictionary. If no parameters remain after filtering,
        returns None.
    """
    if param_grid is None or len(param_grid) == 0:
        return None

    if exclude is None and len(param_grid) > 0:
        return dict(param_grid)

    parsed_param_grid = {}
    for param, grid in param_grid:
        if exclude in param:
            continue

        parsed_param_grid[param] = grid

    return parsed_param_grid
