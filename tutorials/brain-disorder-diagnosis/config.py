from yacs.config import CfgNode

_C = CfgNode()

# Dataset configuration
_C.DATASET = CfgNode()
# Path to the dataset directory
_C.DATASET.PATH = "nilearn_data"
# Name of the brain atlas to use
_C.DATASET.ATLAS = "cc200"
# Whether to apply bandpass filtering
_C.DATASET.BANDPASS = False
# Whether to apply global signal regression
_C.DATASET.GLOBAL_SIGNAL_REGRESSION = False
# Whether to use only quality-checked data
_C.DATASET.QUALITY_CHECKED = False

# Connectivity configuration
_C.CONNECTIVITY = CfgNode()
# List of connectivity measures to compute
_C.CONNECTIVITY.MEASURES = ["pearson"]

# Phenotype configuration
_C.PHENOTYPE = CfgNode()
# How to standardize phenotype data (e.g., by site)
_C.PHENOTYPE.STANDARDIZE = "site"

# Cross-validation configuration
_C.CROSS_VALIDATION = CfgNode()
# Cross-validation split method (e.g., leave-p-groups-out)
_C.CROSS_VALIDATION.SPLIT = "skf"
# Number of folds for cross-validation
_C.CROSS_VALIDATION.NUM_FOLDS = 10
# Number of repeats for cross-validation
_C.CROSS_VALIDATION.NUM_REPEATS = 1

# Trainer configuration
_C.TRAINER = CfgNode()
# Classifier to use (e.g., auto-select)
_C.TRAINER.CLASSIFIER = "lr"
# Use non-linear transformations
_C.TRAINER.NONLINEAR = False
# Search strategy for hyperparameter tuning
_C.TRAINER.SEARCH_STRATEGY = "random"
# Number of iterations for hyperparameter search
_C.TRAINER.NUM_SEARCH_ITER = 100
# Number of iterations for solver
_C.TRAINER.NUM_SOLVER_ITER = int(1e6)
# List of scoring metrics
_C.TRAINER.SCORING = ["accuracy", "roc_auc"]
# Refit based on the best hyperparameters on a scoring metric
_C.TRAINER.REFIT = "accuracy"
# Number of parallel jobs (-1: all CPUs, -4: all but 4 CPUs)
_C.TRAINER.N_JOBS = -4
# Verbosity level
_C.TRAINER.VERBOSE = 0

# Random state for reproducibility
# Seed for random number generators
_C.RANDOM_STATE = 0


def get_cfg_defaults():
    """Get a yacs CfgNode object with default values."""
    return _C.clone()
