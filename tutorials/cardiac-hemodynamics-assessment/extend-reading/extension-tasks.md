# Extension Tasks

## Task 1 - Try different model interpretation settings for ECG
Users can try setting `cfg_FT.INTERPRET.ECG_THRESHOLD=0.8`, `cfg_FT.INTERPRET.ECG_THRESHOLD=0.9`, and `cfg_FT.INTERPRET.ECG_THRESHOLD=0.95` to visualise and compare the top 20%, 10%, and 5% most important features in the 12-lead ECG.

Additionally, users can change the value of `cfg_FT.INTERPRET.ZOOM_RANGE` from 0 to 10 to zoom into specific regions of the input ECG for detailed model interpretation.

## Task 2 - Try different model interpretation settings for CXR
Users can try setting `cfg_FT.INTERPRET.CXR_THRESHOLD=0.8`, `cfg_FT.INTERPRET.CXR_THRESHOLD=0.9`, or `cfg_FT.INTERPRET.CXR_THRESHOLD=0.95` to visualise and compare the top 20%, 10%, and 5% most important features in the CXR.


## Task 3 - Try pre-training with full 50K paired CXR-ECG data (Home task with high resources)
Users can download the [MIMIC-CXR](https://physionet.org/content/mimic-cxr/2.1.0/) and [MIMIC-IV-ECG](https://physionet.org/content/mimic-iv-ecg/1.0/) datasets, then **uncomment** the optional code cell in *Step 1: Data Loading and Preparation*.

Set `cfg_PT.TRAIN.LATENT_DIM=128`, `cfg_PT.DATA.BATCH_SIZE=128` and `cfg_PT.TRAIN.EPOCH=100` to obtain the **optimal pre-trained CardioVAE model** using the full 50K paired CXR-ECG data.
