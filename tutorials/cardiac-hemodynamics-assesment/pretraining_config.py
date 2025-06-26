from yacs.config import CfgNode as CN

_C = CN()

# Data configuration
_C.DATA = CN()
_C.DATA.ECG_PATH = (
    "/content/drive/MyDrive/EMBC_workshop_data/ecg_features_tensor_1000.pt"
)
_C.DATA.CXR_PATH = (
    "/content/drive/MyDrive/EMBC_workshop_data/cxr_features_tensor_1000.pt"
)
_C.DATA.BATCH_SIZE = 128
_C.DATA.NUM_WORKERS = 2

# Model configuration
_C.MODEL = CN()
_C.MODEL.LATENT_DIM = 256
_C.MODEL.INPUT_DIM_ECG = 60000
_C.MODEL.INPUT_DIM_CXR = 1
_C.MODEL.NUM_LEADS = 12

# Training configuration
_C.TRAIN = CN()
_C.TRAIN.EPOCHS = 50
_C.TRAIN.LR = 1e-3
_C.TRAIN.SEED = 123
_C.TRAIN.DEVICE = "cuda"
_C.TRAIN.DATA_DEVICE = "cpu"
_C.TRAIN.LAMBDA_IMAGE = 1.0
_C.TRAIN.LAMBDA_SIGNAL = 10.0
_C.TRAIN.SCALE_FACTOR = 1e-4
_C.TRAIN.SAVE_PATH = "/content/drive/MyDrive/EMBC_workshop_data/cardioVAE.pth"
_C.TRAIN.ACCELERATOR = "gpu"  # or "cpu"
_C.TRAIN.DEVICES = 1  # or 2, 4, "auto", etc.


def get_cfg_defaults():
    return _C.clone()
