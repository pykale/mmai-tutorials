# Helper Functions and Model Definition

## Helper Functions

We provide helper functions that can be inspected directly in the `.py` files located in the notebook's current directory. Two additional helper scripts are:
- [`config.py`](https://github.com/pykale/mmai-tutorial/blob/main/tutorials/multiomics-cancer-classification/config.py): Defines the base configuration settings, which can be overridden using a custom `.yaml` file.
- [`model.py`](https://github.com/pykale/mmai-tutorial/blob/main/tutorials/multiomics-cancer-classification/model.py): Defines the network structure of MOGONET.

## Model Definition in `model.py`
`PyKale` applies `kale.embed` and `kale.predict` to define `MogonetModel` class in [`model.py`](https://github.com/pykale/mmai-tutorials/blob/main/tutorials/multiomics-cancer-classification/model.py), which wraps all the necessary components of the MOGONET pipeline based on the configuration.

This wrapper takes care of:
- Building GCN encoders for each omics modality.
- Creating linear classifiers for modality-specific outputs.
- Optionally initializing a VCDN decoder for multimodal fusion.

MOGONET consists of two major sections: modality-specific encoders to encode graph data into latent space, and View Correlation Discovery Network (VCDN) for multimodal feature fusion, as shown in the top figure.
The modalitity-specific encoders is called from `kale.embed` and VCDN along with the prediction head is integrated in `kale.predict`.

### Embedding Extraction

`PyKale` support graph convolutional neural networks (GCNs) in `kale.embed`, which is used as the modality-specific encoders for MOGONET.
GCNs are neural networks designed for graph data, which generalize convolution operations to graph-structured data by aggregating feature information from neighboring nodes.
Through GCN encoders in `PyKale`, we can encode the raw data to graph embeddings.

### Prediction of Cancer Subtypes

`PyKale` support prediction layers that output the final prediction of cancer subtypes according to the input embeddings.
In `kale.predict`, the VCDN of MOGONET fuses modality-specific predictions for final classification and captures correlations between different modalities at the decision level.
Besides, `PyKale` also call the linear classifier layer from `kale.predict.decode.LinearClassifier` to implement MOGONET.

### Descriptions of Other APIs in [`model.py`](https://github.com/pykale/mmai-tutorials/blob/main/tutorials/multiomics-cancer-classification/model.py)

[`model.py`](https://github.com/pykale/mmai-tutorials/blob/main/tutorials/multiomics-cancer-classification/model.py) also calls `kale.pipeline.multiomics_trainer`, which provides `MultiomicsTrainer`, the training and evaluation engine that orchestrates how unimodal encoders and the multimodal VCDN fusion layer work together. It supports pretraining and full training regimes.
