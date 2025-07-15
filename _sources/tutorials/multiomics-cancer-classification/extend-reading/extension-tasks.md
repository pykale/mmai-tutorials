# Extension Tasks
## Task 1 - Unimodal v.s. Multimodal

Explore using only one modality, e.g., using only mRNA expression, for prediction. You may find the modifying `cfg.DATASET.NUM_MODALITIES` setting in configuration useful for this purpose. Then, compare its results with the ones using all three modalities.

## Task 2 - Explore experiments with another dataset

An additional dataset for Alzheimer's Disease, [**ROSMAP**](https://www.synapse.org/Synapse:syn3219045) [1,2], is provided for further demonstrating the reusability of the code.
A configuration file for **ROSMAP**, named [`configs/ROSMAP.yaml`](https://github.com/pykale/embc-mmai25/blob/main/tutorials/multiomics-cancer-classification/configs/ROSMAP.yaml) has already been provided in the `./configs` folder.

To explore experiments on ROSMAP dataset, replace `"experiments/BRCA.yaml"` with `"experiments/ROSMAP.yaml"` in the following line under [Configuration](https://pykale.github.io/mmai-tutorials/tutorials/multiomics-cancer-classification/tutorial-cancer.html#configuration) section and run the pipeline again.

```python
cfg.merge_from_file("experiments/BRCA.yaml")
```

## Reference

[1] Bennett, D. A., Buchman, A. S., Boyle, P. A., Barnes, L. L., Wilson, R. S., & Schneider, J. A. (2018). Religious orders study and rush memory and aging project. Journal of Alzheimer’s disease, 64(s1), S161-S189.

[2] De Jager, P.L.; Ma, Y.; McCabe, C.; Xu, J.; Vardarajan, B.N.; Felsky, D.; Klein, H.U.; White, C.C.; Peters, M.A.; Lodgson, B.; et al. (2018). A multi-omic atlas of the human frontal cortex for aging and Alzheimer’s disease research. Scientific Data 5, 1-13
