# Helper Functions

Several helper scripts are provided to modularize the code and streamline the workflow. These scripts are located in the [current working directory](https://github.com/pykale/mmai-tutorials/tree/main/tutorials/brain-disorder-diagnosis) of the notebook and can be inspected directly as `.py` files. The helper scripts include:

- [**`config.py`**](https://github.com/pykale/mmai-tutorials/blob/main/tutorials/brain-disorder-diagnosis/config.py): Defines base configuration settings, which can be customized or overridden using external `.yml` files.
- [**`data.py`**](https://github.com/pykale/mmai-tutorials/blob/main/tutorials/brain-disorder-diagnosis/helpers/data.py): Provides data loading functions and utilities for automatically downloading required datasets.
- [**`parsing.py`**](https://github.com/pykale/mmai-tutorials/blob/main/tutorials/brain-disorder-diagnosis/helpers/parsing.py): Contains utilities for compiling and summarizing evaluation results, as well as parsing the hyperparameter grid defined in the configuration.
- [**`preprocess.py`**](https://github.com/pykale/mmai-tutorials/blob/main/tutorials/brain-disorder-diagnosis/helpers/preprocess.py): Handles phenotype preprocessing, including missing value imputation, categorical variable encoding, and FC extraction from the brain signals.
- [**`visualization.py`**](https://github.com/pykale/mmai-tutorials/blob/main/tutorials/brain-disorder-diagnosis/helpers/visualization.py): Provides functions to visualize functional connectivity (FC) examples and the distribution of phenotypic variables.

Throughout the tutorial, we will provide further explanations on the contents and roles of these helper scripts as they are used.

[Back to the main tutorial](https://pykale.github.io/mmai-tutorials/tutorials/brain-disorder-diagnosis/tutorial.html#step-0-environment-preparation)
