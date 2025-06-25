import os
from yacs.config import CfgNode

DEFAULT_DIR = os.path.join(os.getcwd(), "data")

_C = CfgNode()

# Dataset configuration
_C.DATASET = CfgNode()
# Path to the dataset directory
_C.DATASET.PATH = DEFAULT_DIR
# Name of the brain atlas to use
# Available options:
# - "aal" (AAL)
# - "cc200" (Cameron Craddock 200)
# - "cc400" (Cameron Craddock 400)
# - "difumo64" (DiFuMo 64)
# - "dos160" (Dosenbach 160)
# - "hcp-ica" (HCP-ICA)
# - "ho" (Harvard-Oxford)
# - "tt" (Talairach-Tournoux)
_C.DATASET.ATLAS = "cc200"
# Functional connectivity to use
# Available options:
# - "pearson"
# - "partial"
# - "tangent"
# - "precision"
# - "covariance"
# - "tangent-pearson"
_C.DATASET.FC = "tangent-pearson"

# Phenotype configuration
_C.PHENOTYPE = CfgNode()
# How to standardize phenotype data (e.g., by site)
_C.PHENOTYPE.STANDARDIZE = "site"

# Cross-validation configuration
_C.CROSS_VALIDATION = CfgNode()
# Cross-validation split method
# Available options:
# - "skf" (Stratified K-Folds)
# - "lpgo" (Leave-P-Groups-Out)
_C.CROSS_VALIDATION.SPLIT = "skf"
# Number of folds for cross-validation
# or number of groups for Leave-P-Groups-Out
_C.CROSS_VALIDATION.NUM_FOLDS = 10
# Number of repeats for cross-validation
_C.CROSS_VALIDATION.NUM_REPEATS = 5

# Trainer configuration
_C.TRAINER = CfgNode()
# Classifier to use
# Available options:
# - "lda"
# - "lr"
# - "linear_svm"
# - "svm"
# - "ridge"
# - "auto"
_C.TRAINER.CLASSIFIER = "lr"
# Parameter grid for hyperparameter tuning
# We use list of pairs directly instead of CfgNode for flexibility
# As a workaround for yacs limitation, we use None to indicate
# that we're using the large set of default hyperparameters.
_C.TRAINER.PARAM_GRID = None
# Use non-linear transformations (no interpretability)
_C.TRAINER.NONLINEAR = False
# Search strategy for hyperparameter tuning
_C.TRAINER.SEARCH_STRATEGY = "random"
# Number of iterations for hyperparameter search
_C.TRAINER.NUM_SEARCH_ITER = int(1e3)
# Number of iterations for solver
_C.TRAINER.NUM_SOLVER_ITER = int(1e6)
# List of scoring metrics
# Available options:
# - "accuracy"
# - "precision"
# - "recall"
# - "f1"
# - "roc_auc"
# - "matthews_corrcoef"
_C.TRAINER.SCORING = ["accuracy", "roc_auc"]
# Refit based on the best hyperparameters on a scoring metric
_C.TRAINER.REFIT = "accuracy"
# Number of parallel jobs (-1: all CPUs, -4: all but 4 CPUs)
_C.TRAINER.N_JOBS = 1
# Pre-dispatch of jobs for parallel processing
_C.TRAINER.PRE_DISPATCH = "2*n_jobs"
# Verbosity level
_C.TRAINER.VERBOSE = 0

# Random state for reproducibility
# Seed for random number generators
_C.RANDOM_STATE = None


def get_cfg_defaults():
    """Get a yacs CfgNode object with default values."""
    return _C.clone()
