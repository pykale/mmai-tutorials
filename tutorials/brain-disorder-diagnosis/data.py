import os
import json
import numpy as np
import pandas as pd
import gdown

from sklearn.utils._param_validation import StrOptions, validate_params


@validate_params(
    {
        "data_dir": [str],
        "atlas": [
            StrOptions(
                {
                    "aal",
                    "cc200",
                    "difumo64",
                    "dos160",
                    "hcp-ica",
                    "ho",
                    "tt",
                }
            )
        ],
        "fc": [
            StrOptions(
                {
                    "pearson",
                    "partial",
                    "tangent",
                    "precision",
                    "covariance",
                    "tangent-pearson",
                }
            )
        ],
        "vectorize": [bool],
        "verbose": [bool],
    },
    prefer_skip_nested_validation=False,
)
def load_data(
    data_dir="data", atlas="cc200", fc="tangent-pearson", vectorize=True, verbose=True
):
    """
    Load functional connectivity data and phenotypic data with gdown support.

    This function uses manifest files to download the required files from Google Drive if not present locally.
    It automatically downloads files listed in manifests/abide.json and folders listed in manifests/atlas.json.

    Parameters
    ----------
    data_dir : str, optional (default="data")
        Local directory to store the dataset.

    atlas : str, optional (default="cc200")
        Atlas name (subfolder inside fc/).

    fc : str, optional (default="tangent-pearson")
        Functional connectivity file name (without extension).

    vectorize : bool, optional (default=True)
        Whether to vectorize the upper triangle of the connectivity matrices.

    verbose : bool, optional (default=True)
        Whether to print download and progress messages.

    Returns
    -------
    fc_data : np.ndarray
        Functional connectivity data (vectorized if requested).

    phenotypes : pd.DataFrame
        Loaded phenotypic data.

    rois : np.ndarray
        ROI labels.

    coords : np.ndarray
        ROI coordinates.

    Raises
    ------
    FileNotFoundError
        If the required file paths are not found after attempted download.
    """
    # Paths
    fc_path = os.path.join(data_dir, "abide", "fc", atlas, f"{fc}.npy")
    is_proba = atlas in {"difumo64"}
    atlas_type = "probabilistic" if is_proba else "deterministic"
    atlas_path = os.path.join(data_dir, "atlas", atlas_type, atlas)
    phenotypes_path = os.path.join(data_dir, "abide", "phenotypes.csv")

    # Ensure all files exist (download if needed)
    _ensure_abide_file(data_dir, fc_path, verbose)
    _ensure_abide_file(data_dir, phenotypes_path, verbose)
    _ensure_atlas_folder(data_dir, atlas_path, verbose)

    # Load connectivity data
    fc_data = np.load(fc_path)
    if vectorize:
        row, col = np.triu_indices(fc_data.shape[1], 1)
        fc_data = fc_data[..., row, col]

    phenotypes = pd.read_csv(phenotypes_path)

    with open(os.path.join(atlas_path, "labels.txt"), "r") as f:
        rois = np.array(f.read().strip().split("\n"))
    coords = np.load(os.path.join(atlas_path, "coords.npy"))

    return fc_data, phenotypes, rois, coords


def _ensure_abide_file(data_dir, target_path, verbose):
    """Ensure abide file exists locally; download from manifest if missing."""
    if os.path.exists(target_path):
        if verbose:
            print(f"✔ File found: {target_path}")
        return

    manifest_path = os.path.join(os.path.dirname(__file__), "manifests", "abide.json")
    with open(manifest_path, "r") as f:
        manifest = json.load(f)

    rel_path = os.path.relpath(target_path, data_dir).replace("\\", "/")
    for file_entry in manifest:
        if file_entry["path"] == rel_path:
            if verbose:
                print(f"⬇ Downloading {rel_path} ...")
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            gdown.download(file_entry["url"], output=target_path, quiet=not verbose)
            if os.path.exists(target_path):
                return
            else:
                break

    raise FileNotFoundError(f"File not found and not found in manifest: {target_path}")


def _ensure_atlas_folder(data_dir, atlas_path, verbose):
    """Ensure atlas folder exists locally; download using gdown.download_folder if missing."""
    if os.path.exists(atlas_path):
        if verbose:
            print(f"✔ Atlas folder found: {atlas_path}")
        return

    manifest_path = os.path.join("manifests", "atlas.json")
    with open(manifest_path, "r") as f:
        manifest = json.load(f)

    rel_path = os.path.relpath(atlas_path, data_dir).replace("\\", "/")
    for folder_entry in manifest:
        if folder_entry["path"] == rel_path:
            if verbose:
                print(f"⬇ Downloading atlas folder {rel_path} ...")
            os.makedirs(os.path.dirname(atlas_path), exist_ok=True)
            gdown.download_folder(
                id=folder_entry["id"], output=atlas_path, quiet=not verbose
            )
            if os.path.exists(atlas_path):
                return
            else:
                break

    raise FileNotFoundError(
        f"Atlas folder not found and not found in manifest: {atlas_path}"
    )
