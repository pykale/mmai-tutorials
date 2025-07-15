# Extension Tasks
## Task 1 - Unimodal v.s. Multimodal
Users can try to set the `cfg.DATASET.NUM_MODALITIES=1` to try only using single mRNA experission for prediction and compare its results with the ones using all three modalities.

## Task 2 - Try another dataset
To demonstrate the generalizability of the model, we also provide a dataset for Alzheimer's Disease, [**ROSMAP**](https://www.synapse.org/Synapse:syn3219045) [1,2]
Besides, we also provide a configuration file for **ROSMAP**, named [`configs/ROSMAP.yaml`](https://github.com/pykale/embc-mmai25/blob/main/tutorials/multiomics-cancer-classification/configs/ROSMAP.yaml).

To try ROSMAP dataset, replace `"experiments/BRCA.yaml"` with `"experiments/ROSMAP.yaml"` in the following line under Configuration section and run the pipeline again.
```python
cfg.merge_from_file("experiments/BRCA.yaml")
```
## Reference
[1] Bennett, D. A., Buchman, A. S., Boyle, P. A., Barnes, L. L., Wilson, R. S., & Schneider, J. A. (2018). Religious orders study and rush memory and aging project. Journal of Alzheimer’s disease, 64(s1), S161-S189.

[2] De Jager, P.L.; Ma, Y.; McCabe, C.; Xu, J.; Vardarajan, B.N.; Felsky, D.; Klein, H.U.; White, C.C.; Peters, M.A.; Lodgson, B.; et al. (2018). A multi-omic atlas of the human frontal cortex for aging and Alzheimer’s disease research. Scientific Data 5, 1-13