from yacs.config import CfgNode as CN

_C = CN()

# Data configuration
_C.DATA = CN()
_C.DATA.ECG_PATH = "/content/drive/MyDrive/EMBC_workshop_data/ecg_features_tensor_last_1000.pt"
_C.DATA.CXR_PATH = "/content/drive/MyDrive/EMBC_workshop_data/cxr_features_tensor_last_1000.pt"
_C.DATA.CSV_PATH = "/content/drive/MyDrive/EMBC_workshop_data/chexpert_healthy_abnormality_subset.csv"
_C.DATA.BATCH_SIZE = 32
_C.DATA.NUM_WORKERS = 2
_C.DATA.DATA_DEVICE = "cpu"

# Model configuration
_C.MODEL = CN()
_C.MODEL.LATENT_DIM = 256
_C.MODEL.INPUT_IMAGE_CHANNELS = 1
_C.MODEL.INPUT_DIM_ECG = 60000
_C.MODEL.NUM_LEADS = 12

# Fine-tuning configuration
_C.FT = CN()
_C.FT.EPOCHS = 15
_C.FT.LR = 0.001
_C.FT.HIDDEN_DIM = 128
_C.FT.NUM_CLASSES = 2
_C.FT.CKPT_PATH = "/content/drive/MyDrive/EMBC_workshop_data/CardioVAE.pth"
_C.FT.ACCELERATOR = "gpu"
_C.FT.DEVICES = 1           # This is for PyTorch Lightning's Trainer, set as int not string
_C.FT.DEVICE = "cuda"       # For torch.device()
_C.FT.KFOLDS = 5
_C.FT.SEED = 42

# Interpretation configuration
_C.INTERPRET = CN()
_C.INTERPRET.SAMPLE_IDX = 101
_C.INTERPRET.ZOOM_RANGE = [3, 3.5]
_C.INTERPRET.ECG_THRESHOLD = 0.7
_C.INTERPRET.CXR_THRESHOLD = 0.7
_C.INTERPRET.LEAD_NUMBER = 12
_C.INTERPRET.SAMPLING_RATE = 500

def get_cfg_defaults():
    return _C.clone()
