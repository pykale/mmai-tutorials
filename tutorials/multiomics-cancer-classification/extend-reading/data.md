# Organization of Input Data

To help users better understand the format and organization of the input data, we provide example data under [data-example folder](https://github.com/pykale/tutorials/multiomics-cancer-classification/data-example).

For each modality/omics, the raw data is separated into five files:
- [`{}_feat_name.csv`](https://github.com/pykale/tutorials/multiomics-cancer-classification/data-example/1_feat_name.csv): Names of all features of current modality. Each row represents one example.
- `{}_lbl_te.csv`: Labels of test set.
- `{}_lbl_tr.csv`: Labels of training set.
- `{}_te.csv`: Values of all features for test examples. Each row is one example and each column is one feature. In this tutorial, it is the normalized gene expression level for mRNA and miRNA, and is $\beta$ value for DNA methylation.
- `{}_tr.csv`: Values of all features for training examples. Each row is one example and each column is one feature. In this tutorial, it is the normalized gene expression level for mRNA and miRNA, and is $\beta$ value for DNA methylation.

Within in `{}` is the index of the modality, starting from 1. For example, if user has two modalities, the files are named as `1_feat_name.csv`, ..., `2_feat_name.csv`, ...