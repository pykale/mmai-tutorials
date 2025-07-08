# Extension Tasks
## Task 1 - Unimodal v.s. Multimodal
Users can try to set the `cfg.DATASET.NUM_MODALITIES=1` to try only using single mRNA experission for prediction and compare its results with the ones using all three modalities.

## Task 2 - Try another dataset
To try ROSMAP dataset, replace `"experiments/BRCA.yaml"` with `"experiments/ROSMAP.yaml"` in the following line under Configuration section and run the pipeline again.
```python
cfg.merge_from_file("experiments/BRCA.yaml")
```
