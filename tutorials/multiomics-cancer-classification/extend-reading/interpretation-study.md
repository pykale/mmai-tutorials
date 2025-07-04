# Interpretation Study - Feature Masking Importance Analysis
To better understand which features among multiomics data are the key biomarkers in cancer subtype classification and how decisions were made by the model, we perform an interpretation study to identify important biomarkers.
We identify the most influential features (biomarkers) using **feature-masking-based importance analysis**.

We use `kale.interpret` to perform interpretation, where a function that systematically masks input features and observes the effect on performance—highlighting which features are most important for classification is provided.

## How Feature Importance Is Computed?
The `select_top_features_by_masking` function in `PyKale` implements a feature ablation approach to estimate feature importance for multi-omics data.

For each feature in each modality:

- Temporarily mask (zero out) the feature.

- Evaluate the model on the test set.

- Measure the performance drop (e.g., in F1 score). The larger the drop, the more important the feature is.

- Importance is calculated as $Importance_j=(FullMetric-MaskedMetric_j)\times d$,
where $j$ is the feature index and $d$ is the number of features in the modality (to scale the effect)
For demonstration, we use **F1 score** as the metric to calculate feature importance.

## Full results of interpretation study

We attach the full results of most important features reported in the original paper for reference:

**Table 3**: Important features in BRCA dataset.

|      Omics       | Importance features |
|:----------------:|:---------------------------------------------:|
| mRNA expression  |       SOX11, AMY1A, SLC6A15, FABP7, SLC6A14, SLC6A2, FGFBP1, DSG1, UGT8, ANKRD45, PI3, SERPINB5, COL11A2, ARHGEF4, SOX10    |
| DNA methylation  |       GPR37L1, MIR563, OR1J4, ATP10B, KRTAP3-3, FLJ41941, TMEM207, CDH26, MT1DP    |
| miRNA expression |       hsa-mir-205, hsa-mir-187, hsa-mir-452, hsa-mir-20b, hsa-mir-224, hsa-mir-204    |

**Table 4**: Important features in ROSMAP dataset.

|      Omics       | Importance features |
|:----------------:|:---------------------------------------------:|
| mRNA expression  |       NPNT, CDK18, KIF5A, SPACA6, TCEA3, SYTL1, ARRDC2, APLN    |
| DNA methylation  |       TMC4, AGA, HYAL2, CCL3, TTC15    |
| miRNA expression |       hsa-miR-423-3p, hsa-miR-33a, hsa-miR-640, hsa-miR-362-3p, hsa-miR-491-5p, hsa-miR-206, hsa-miR-548b-3p, hsa-miR-127-3p, hsa-miR-106a_hsa-miR-17, hsa-miR-424, hsa-miR-577, hsa-miR-873, hsa-miR-651, hsa-miR-199b-5p, hsa-miR-192, hsa-miR-199a-5p, hsv1-miR-H1    |
