# a dummy config file
from yacs.config import CfgNode


_C = CfgNode()

# Dataset configuration
_C.DATASET = CfgNode()
# Path to the dataset directory
_C.DATASET.DATA_DIR = "/content/"


# Model configuration
_C.MODEL = CfgNode()
# Type of model to use
_C.MODEL.NAME = "MyModel"


def get_cfg_defaults():
    """Get a yacs CfgNode object with default values."""
    return _C.clone()
