import numpy as np
import polars as pl
from sklearn.preprocessing import StandardScaler
from sklearn.utils._param_validation import StrOptions, validate_params

__all__ = ["preprocess_phenotypic_data", "extract_functional_connectivity"]

CATEGORICAL_PHENOTYPES = ["SITE_ID", "SEX", "HANDEDNESS_CATEGORY", "EYE_STATUS_AT_SCAN"]
CONTINUOUS_PHENOTYPES = ["AGE_AT_SCAN", "FIQ"]


@validate_params(
    {
        "data": [pl.DataFrame],
        "standardize": [StrOptions({"site", "all"}), "boolean"],
    },
    prefer_skip_nested_validation=False,
)
def preprocess_phenotypic_data(data, standardize=False):
    """
    Preprocess phenotypic data by encoding labels, one-hot encoding categorical variables,
    and optionally standardizing continuous variables.

    Parameters
    ----------
    data : pl.DataFrame
        The input phenotypic dataframe containing both labels and covariates.
    standardize : {'site', 'all', True, False}, optional
        Strategy for standardizing continuous variables:
        - 'site': standardize AGE_AT_SCAN and FIQ within each site.
        - 'all' or True: standardize AGE_AT_SCAN and FIQ across all subjects.
        - False (default): no standardization applied.

    Returns
    -------
    labels : np.ndarray of shape (n_subjects,)
        Binary classification labels encoded as 0 (CONTROL) and 1 (ASD).
    sites : np.ndarray of shape (n_subjects,)
        Site identifiers for each subject.
    phenotypes : pl.DataFrame
        Preprocessed phenotypic features, with categorical variables one-hot encoded
        and continuous variables optionally standardized.
    """
    # Encode labels
    labels = data["DX_GROUP"].replace({"CONTROL": 0, "ASD": 1})
    labels = labels.cast(pl.Int8).to_numpy()

    # Extract site information
    sites = data["SITE_ID"].to_numpy()

    # Drop label column before feature processing
    data = data.drop("DX_GROUP")

    # One-hot encode categorical phenotypes
    data = data.to_dummies(CATEGORICAL_PHENOTYPES)

    if standardize == "site":
        sites_unique = np.unique(sites)
        scaled_data = []

        for site in sites_unique:
            # Select data for the current site
            site_data = data.filter(sites == site)

            values = site_data.select(CONTINUOUS_PHENOTYPES).to_numpy()
            scaler = StandardScaler()
            values_scaled = scaler.fit_transform(values)
            age, fiq = values_scaled.T

            scaled_site_data = site_data.with_columns(
                [pl.Series("AGE_AT_SCAN", age), pl.Series("FIQ", fiq)]
            )

            scaled_data.append(scaled_site_data)

        data = pl.concat(scaled_data)

    elif standardize:
        values = data.select(CONTINUOUS_PHENOTYPES).to_numpy()
        scaler = StandardScaler()
        values_scaled = scaler.fit_transform(values)
        age, fiq = values_scaled.T

        data = data.with_columns(
            [
                pl.Series("AGE_AT_SCAN", age),
                pl.Series("FIQ", fiq),
            ]
        )

    data = data.sort("SUB_ID").drop("SUB_ID")
    phenotypes = data.to_numpy()

    return labels, sites, phenotypes


@validate_params(
    {"data": ["array-like"], "measures": [list]}, prefer_skip_nested_validation=False
)
def extract_functional_connectivity(data, measures=["pearson"]):
    """
    Extract functional connectivity features from time series data using
    specified connectivity measures.

    To extract Tangent-Pearson connectivity, set `measures=["tangent", "pearson"]`.

    Parameters
    ----------
    data : list[array-like] of shape (n_subjects,)
        An array of numpy arrays, where each array is a time series of shape (t, n_rois).
        The time series data for each subject.
    measures : list[str], optional (default=["pearson"])
        A list of connectivity measures to use for feature extraction.
        Supported measures are "pearson", "partial", "tangent", "covariance", and "precision".
        Multiple measures can be specified as a list to compose a higher-order measure.

    Returns
    -------
    features : array-like
        An array of shape (n_subjects, n_features) containing the extracted features.
        n_features is equal to `n_rois * (n_rois - 1) / 2` for each subject if vectorized.
    """
    for i, k in enumerate(reversed(measures), 1):
        k = AVAILABLE_FC_MEASURES.get(k)

        islast = i == len(measures)
        measure = ConnectivityMeasure(kind=k, vectorize=islast, discard_diagonal=islast)
        data = measure.fit_transform(data)

    return data
