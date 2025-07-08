# Data

## Data Organization

To help users better understand the format and organization of the input data, we provide example data under [data-example folder](https://github.com/pykale/mmai-tutorials/blob/main/tutorials/multiomics-cancer-classification/data-example/).

For each modality/omics, the raw data is separated into five files:
- [`{}_feat_name.csv`](https://github.com/pykale/mmai-tutorials/blob/main/tutorials/multiomics-cancer-classification/data-example/1_feat_name.csv): Names of all features of current modality. Each row represents one example.
- [`{}_lbl_te.csv`](https://github.com/pykale/mmai-tutorials/blob/main/tutorials/multiomics-cancer-classification/data-example/1_lbl_te.csv): Labels of test set.
- [`{}_lbl_tr.csv`](https://github.com/pykale/mmai-tutorials/blob/main/tutorials/multiomics-cancer-classification/data-example/1_lbl_tr.csv): Labels of training set.
- [`{}_te.csv`](https://github.com/pykale/mmai-tutorials/blob/main/tutorials/multiomics-cancer-classification/data-example/1_te.csv): Values of all features for test examples. Each row is one example and each column is one feature. In this tutorial, it is the normalized gene expression level for mRNA and miRNA, and is $\beta$ value for DNA methylation.
- [`{}_tr.csv`](https://github.com/pykale/mmai-tutorials/blob/main/tutorials/multiomics-cancer-classification/data-example/1_tr.csv): Values of all features for training examples. Each row is one example and each column is one feature. In this tutorial, it is the normalized gene expression level for mRNA and miRNA, and is $\beta$ value for DNA methylation.

Within in `{}` is the index of the modality, starting from 1. For example, if user has two modalities, the files are named as `1_feat_name.csv`, ..., `2_feat_name.csv`, ...

After organizing the data, please don't foget to change `DATASET.NUM_MODALITIES` to the specific number of modalities in `.yaml` file.

## Description of Datasets in Tutorial

A brief description of BRCA and ROSMAP dataset is shown in the following
table.

**Table 1**: Characteristics of the preprocessed BRCA multiomics dataset.

|      Omics       | #Training samples | #Test samples | #Features |
|:----------------:|:-----------------:|:-------------:|:---------:|
| mRNA expression  |        612        |      263      |   1000    |
| DNA methylation  |        612        |      263      |   1000    |
| miRNA expression |        612        |      263      |    503    |

**Table 2**: Characteristics of the preprocessed ROSMAP multiomics dataset.

|      Omics       | #Training samples | #Test samples | #Features  |
|:----------------:|:-----------------:|:-------------:|:----------:|
| mRNA expression  |        245        |      106      |    200     |
| DNA methylation  |        245        |      106      |    200     |
| miRNA expression |        245        |      106      |    200     |

## Data Downloading, Loading, and Pre-processing
The data downloading function has been integrated in `kale.loaddata.multiomics_datasets.SparseMultiomicsDataset`, which also included loading data from the raw `.csv` files and pre-processing data to the graphs we needed.

This function transforms tabular multiomics data into graph datasets by treating each patient sample as a node and using molecular measurements as node features. For each modality, it reads feature matrices and labels from `.csv` files, splits them into training and test sets.

Then, it samples similaity networks from the graphs as shown in the top figure. It computes sample similarities to define edges between nodes. These similarities are used to construct sparse adjacency matrices, where only the most relevant connections are retained.

Next, each graph is represented with node features, edge connections, and labels, encapsulating both feature and relational structure for downstream graph-based learning.
