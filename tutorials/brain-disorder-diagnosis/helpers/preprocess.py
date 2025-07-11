import logging

import numpy as np
import pandas as pd
from nilearn.connectome import ConnectivityMeasure
from sklearn.preprocessing import StandardScaler
from sklearn.utils._param_validation import (
    Integral,
    Interval,
    StrOptions,
    validate_params,
)

__all__ = ["preprocess_phenotypic_data", "extract_functional_connectivity"]

SELECTED_PHENOTYPES = [
    "SUB_ID",
    "SITE_ID",
    "SEX",
    "AGE_AT_SCAN",
    "FIQ",
    "HANDEDNESS_CATEGORY",
    "EYE_STATUS_AT_SCAN",
    "DX_GROUP",
]

MAPPING = {
    "SEX": {1: "MALE", 2: "FEMALE"},
    "HANDEDNESS_CATEGORY": {
        "L": "LEFT",
        "R": "RIGHT",
        "Mixed": "AMBIDEXTROUS",
        "Ambi": "AMBIDEXTROUS",
        "L->R": "AMBIDEXTROUS",
        "R->L": "AMBIDEXTROUS",
        "-9999": "RIGHT",
        np.nan: "RIGHT",
    },
    "EYE_STATUS_AT_SCAN": {1: "OPEN", 2: "CLOSED"},
    "DX_GROUP": {1: "ASD", 2: "CONTROL"},
}

AVAILABLE_FC_MEASURES = {
    "pearson": "correlation",
    "partial": "partial correlation",
    "tangent": "tangent",
    "covariance": "covariance",
    "precision": "precision",
}


@validate_params(
    {
        "data": [pd.DataFrame],
        "standardize": [StrOptions({"site", "all"}), "boolean"],
        "one_hot_encode": ["boolean"],
    },
    prefer_skip_nested_validation=False,
)
def preprocess_phenotypic_data(data, standardize=False, one_hot_encode=True):
    """Process phenotypic data to impute missing values and and encode categorical
    variables including sex, handedness, eye status at scan, and diagnostic group.

    Parameters
    ----------
    data : pd.DataFrame of shape (n_subjects, n_phenotypes)
        The phenotypes data to be processed.

    standardize : boolean or str of ("site", "all"), (default=False)
                Standardize FIQ and age. Setting to True or "all"
                standardizes the values over all subjects while "site"
                standardizes according to the site.

    one_hot_encode : boolean (default=True)
                Whether to one-hot encode categorical variables in the phenotypes.

    Returns
    -------
    labels : array-like of shape (n_subjects)
            The encoded classification group. 0 is "CONTROL" and
            1 is "ASD"

    sites : array-like of shape (n_subjects)
            The site IDs for each subject.

    phenotypes : pd.DataFrame of shape (n_subjects, n_selected_phenotypes)
                The processed selected phenotype data with imputed values.
    """
    # Avoid in-place modification
    data = data.copy()

    # Check for missing values, either -9999 or NaN
    # and impute them with FIQ = 100 following original code.
    fiq = data["FIQ"].copy()
    data["FIQ"] = fiq.where((fiq != -9999) & (~np.isnan(fiq)), 100)

    # Standardize FIQ and age by site
    if standardize == "site":
        for site in data["SITE_ID"].unique():
            mask = site == data["SITE_ID"]
            values = data.loc[mask, ["AGE_AT_SCAN", "FIQ"]]
            values = StandardScaler().fit_transform(values)
            data.loc[mask, ["AGE_AT_SCAN", "FIQ"]] = values
    elif standardize:
        values = data.loc[:, ["AGE_AT_SCAN", "FIQ"]]
        values = StandardScaler().fit_transform(values)
        data.loc[:, ["AGE_AT_SCAN", "FIQ"]] = values

    # Encode categorical variables to be more explicit categorical
    # values. For handedness, if we found missing values, we
    # impute them by using 'LEFT' as default. Values
    # like 'Ambi', 'Mixed', 'L->R', and 'R->L' are mapped to
    # 'AMBIDEXTROUS'. The rest of the values are mapped to 'LEFT' or 'RIGHT'
    # for 'L' or 'R' respectively.
    for key in MAPPING:
        values = data[key].copy().map(MAPPING[key])
        data[key] = values.astype("category")

    # Subsets the phenotypes
    data = data[SELECTED_PHENOTYPES].set_index("SUB_ID")

    # Separate the class labels, sites, and phenotypes
    labels = data["DX_GROUP"].map({"CONTROL": 0, "ASD": 1}).to_numpy()
    sites = data["SITE_ID"].to_numpy()
    phenotypes = data.drop(columns=["DX_GROUP"])
    # One-hot encode categorical valued phenotypes
    if one_hot_encode:
        phenotypes = pd.get_dummies(phenotypes)

    return labels, sites, phenotypes


@validate_params(
    {"data": ["array-like"], "measures": [list, tuple]},
    prefer_skip_nested_validation=False,
)
def extract_functional_connectivity(data, measures=["pearson"]):
    """Extract functional connectivity features from time series data.

    Parameters
    ----------
    data : list[array-like] or tuple[array-like] of shape (n_subjects,)
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
        n_features is equal to `n_rois * (n_rois - 1) / 2` for each subjects.
    """
    for i, k in enumerate(reversed(measures), 1):
        try:
            k = AVAILABLE_FC_MEASURES.get(k)
        except KeyError:
            raise ValueError(
                f"Unsupported connectivity measure '{k}' in {measures}. "
                f"Available options are: {', '.join(AVAILABLE_FC_MEASURES.keys())}."
            )

        # If it is the last transformation, vectorize and discard the diagonal
        # of shape (n_rois * (n_rois - 1) / 2)
        islast = i == len(measures)
        measure = ConnectivityMeasure(kind=k, vectorize=islast, discard_diagonal=islast)
        data = measure.fit_transform(data)

    return data
