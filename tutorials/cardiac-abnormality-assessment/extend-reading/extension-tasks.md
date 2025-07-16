# Extension Tasks

## Task 1 - Explore different model interpretation settings for CXR and ECG

Visualise and compare the top 20%, 10%, and 5% most important features in the 12-lead ECG. You may find the modifying values for `cfg_FT.INTERPRET.ECG_THRESHOLD` and `cfg_FT.INTERPRET.CXR_THRESHOLD` in configuration useful for this purpose.

## Task 2 - Zoom into specific regions of the input ECG

Zoom into specific regions of the input ECG for detailed model interpretation. You can set different values for `cfg_FT.INTERPRET.ZOOM_RANGE` for this task.


## Task 3 - Explore pre-training with full 50K paired CXR-ECG data (Home task with high resources)

Download the [MIMIC-CXR](https://physionet.org/content/mimic-cxr/2.1.0/) and [MIMIC-IV-ECG](https://physionet.org/content/mimic-iv-ecg/1.0/) datasets, then **uncomment** the optional code cell in *[Step 1: Data Loading and Preparation](https://pykale.github.io/mmai-tutorials/tutorials/cardiac-abnormality-assessment/tutorial-heart.html#step-1-data-loading-and-preparation)*.

Set `cfg_PT.TRAIN.LATENT_DIM=128`, `cfg_PT.DATA.BATCH_SIZE=128` and `cfg_PT.TRAIN.EPOCH=100` to obtain the **optimal pre-trained CardioVAE model** using the full 50K paired CXR-ECG data. Compare the results with the pre-trained CardioVAE model using 1K paired CXR-ECG data in the tutorial.
