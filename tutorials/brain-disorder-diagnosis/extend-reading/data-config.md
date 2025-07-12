# Data and Configuration Arguments

## Configuration Arguments for Data Loading

When using configuration files, remember that all parameter names must be specified in **uppercase** per `yacs` convention.

The available argument we mainly focused on includes:

- **`data_dir`**: Local directory to store and load the dataset. If files are missing, they will be automatically downloaded.
  - *Default:* Current working directory + `/data`

- **`atlas`**: The name of the brain atlas used to extract ROI time series. This corresponds to a subfolder inside `fc/`.
  - Available options:
    - `"aal"`: AAL Atlas
    - `"cc200"`: Craddock 200 ROI Atlas
    - `"cc400"`: Craddock 400 ROI Atlas
    - `"difumo64"`: DiFuMo 64 components
    - `"dos160"`: Dosenbach 160 Atlas
    - `"hcp-ica"`: HCP ICA-based components
    - `"ho"`: Harvard-Oxford Atlas
    - `"tt"`: Talairach-Tournoux
  - *Default:* `"cc200"`

- **`fc`**: The type of functional connectivity embedding to load (file name without extension).
  - Available options:
    - `"pearson"`: Pearson correlation
    - `"partial"`: Partial correlation
    - `"tangent"`: Tangent embedding
    - `"precision"`: Precision (inverse covariance)
    - `"covariance"`: Sample covariance
    - `"tangent-pearson"`: Hybrid of tangent embedding and Pearson correlation
  - *Default:* `"tangent-pearson"`

- **`top_k_sites`**: Optionally restrict the dataset to the top *K* sites (by number of subjects). If `None`, all sites are included.
  - *Default:* `None`

It returns four values, including:

- **`fc_data`** (`np.ndarray`): Functional connectivity data (vectorized if `vectorize=True`).

- **`phenotypes`** (`pd.DataFrame`): Associated phenotypic information (e.g., site, age, gender).

- **`rois`** (`np.ndarray`): ROI labels associated with the selected atlas.

- **`coords`** (`np.ndarray`): ROI coordinates for visualization purposes.

[Back to the main tutorial](https://pykale.github.io/mmai-tutorials/tutorials/brain-disorder-diagnosis/tutorial.html#data-loading)

## Categorical Variables from Phenotypic Data

The following categorical phenotypes are included and will be **one-hot encoded** for modeling:

- `SITE_ID`
- `SEX`
- `HANDEDNESS_CATEGORY`
- `EYE_STATUS_AT_SCAN`

These variables are first mapped to descriptive labels using the provided `MAPPING` dictionary:

- `SEX`: `{1 → MALE, 2 → FEMALE}`
- `HANDEDNESS_CATEGORY`: Includes various representations unified into:
  - `"RIGHT"` (including missing values and `-9999`)
  - `"LEFT"`
  - `"AMBIDEXTROUS"` (e.g., `"Mixed"`, `"L->R"`, `"Ambi"`)
- `EYE_STATUS_AT_SCAN`: `{1 → OPEN, 2 → CLOSED}`

**Continuous Variables**

The following continuous phenotypes will be optionally **standardized**:

- `AGE_AT_SCAN`
- `FIQ`

We will explain the available options for standardizing these phenotypes in more detail down below.

**Handling Missing Values**

Missing values are handled with the following assumptions and imputation strategies:

- `HANDEDNESS_CATEGORY`: Missing entries (`-9999` or `NaN`) are imputed as `"RIGHT"`.
- `FIQ`: Missing scores (`-9999`) are imputed with a default value of `100`.

These choices ensure that the downstream models can operate without interruption while maintaining reasonable assumptions based on domain knowledge.

**Target Variable Encoding**

The diagnostic group `DX_GROUP` is used to define the target label for classification:

- `CONTROL` → `0`
- `ASD` → `1`

This binary label is suitable for supervised learning tasks focused on ASD detection.

To do this, the `preprocess_phenotypic_data` function handles this functionality for us.
The main arguments for `preprocess_phenotypic_data` include:

- **`data`**:
  A DataFrame containing the phenotypic information for each subject. Must include all selected phenotypes such as `SEX`, `AGE_AT_SCAN`, `FIQ`, `HANDEDNESS_CATEGORY`, `EYE_STATUS_AT_SCAN`, and `DX_GROUP`.
  - *Type:* `pd.DataFrame` of shape `(n_subjects, n_phenotypes)`
  - *Required*

- **`standardize`**:
  Whether to standardize continuous variables (`AGE_AT_SCAN` and `FIQ`). This helps remove scale-related bias before modeling.
  - Available options:
    - `False`: No standardization (raw values retained)
    - `True` or `"all"`: Standardize across all subjects
    - `"site"`: Standardize within each acquisition site
  - *Default:* `False`

- **`one_hot_encode`**:
  Whether to one-hot encode categorical variables (`SITE_ID`, `SEX`, `HANDEDNESS_CATEGORY`, `EYE_STATUS_AT_SCAN`). This is typically used when feeding the data into machine learning models.
  - *Type:* `bool`
  - *Default:* `True`

The function returns the following:

- **`labels`** (`array-like`):
  The encoded diagnostic labels derived from `DX_GROUP`.
  - `0`: CONTROL
  - `1`: ASD
  - *Shape:* `(n_subjects,)`

- **`sites`** (`array-like`):
  Site identifiers corresponding to each subject, useful for site-wise stratification or harmonization.
  - *Shape:* `(n_subjects,)`

- **`phenotypes`** (`pd.DataFrame`):
  The cleaned and processed phenotype DataFrame with missing values imputed, categorical variables mapped (and optionally one-hot encoded), and continuous variables optionally standardized.
  - *Shape:* `(n_subjects, n_selected_phenotypes)`
  - *Note:* The selected phenotypes include:
    - `SITE_ID`
    - `SEX`
    - `AGE_AT_SCAN`
    - `FIQ`
    - `HANDEDNESS_CATEGORY`
    - `EYE_STATUS_AT_SCAN`

[Back to the main tutorial](https://pykale.github.io/mmai-tutorials/tutorials/brain-disorder-diagnosis/tutorial.html#data-preprocessing)

## Configuration Arguments for Cross-Validation

In this tutorial, we specify the following arguments for cross-validation:
- **`split`**: Defines the cross-validation strategy.
  - Available options:
    - `"skf"`: Stratified K-fold to maintain label balance in each fold.
    - `"lpgo"`: Leave p-groups out to evaluate generalization across sites by holding out entire groups (e.g., imaging sites).
  - *Default:* `"skf"`

- **`num_folds`**: The number of folds for `"skf"` or the number of groups to leave out in `"lpgo"`.
  - *Default:* `10`

- **`num_repeats`**: The number of times the k-fold procedure is repeated to obtain more stable estimates (ignored with `"lpgo"`).
  - *Default:* `5`

- **`random_state`**: Seed for random number generators for reproducibility.
  - *Default:* `None`

[Back to the main tutorial](https://pykale.github.io/mmai-tutorials/tutorials/brain-disorder-diagnosis/tutorial.html#cross-validation-split)

## Hyperparameter Grid

We also specify the hyperparameter search strategy and other training parameters for each configuration, including:

- **`classifier`**: The base model used for classification.
  - Available options:
    - `"lda"`: Linear Discriminant Analysis
    - `"lr"`: Logistic Regression
    - `"linear_svm"`: Linear Support Vector Machine
    - `"svm"`: Kernel Support Vector Machine
    - `"ridge"`: Ridge Classifier (L2-regularized linear model)
    - `"auto"`: Automatically selects an appropriate model based on data characteristics.
  - *Default:* `"lr"`

- **`param_grid`**: The hyperparameter grid used for both the classifier and the MIDA domain adapter.
  - To specify MIDA’s parameters, each key in the grid must be prefixed with `domain_adapter__` (e.g., `domain_adapter__mu`).
  - For classifier parameters, no prefix is needed.
  - If `param_grid` is set to `None`, PyKale will use its default grid, which spans a broad hyperparameter search space. While this may maximize performance, it significantly increases training time.
  - Therefore, it is **not recommended** to use `param_grid=None` in combination with `search_strategy='grid'`.
  - *Default:* `None`

- **`nonlinear`**: Whether to apply non-linear transformations (non-interpretable).
  - *Type:* `boolean`
  - *Default:* `False`

- **`search_strategy`**: The hyperparameter search method.
  - Available options:
    - `"random"`: Randomly search over finite iterations.
    - `"grid"`: Search over all possible combinations.
  - *Default:* `"random"`

- **`num_search_iterations`**: The number of hyperparameter combinations to evaluate in randomized search.
  - *Default:* `1,000`

- **`num_solver_iterations`**: The maximum number of iterations allowed for solver convergence.
  - *Default:* `1,000,000`

- **`scoring`**: A list of performance metrics used during cross-validation.
  - Available options:
    - `"accuracy"`: Accuracy
    - `"precision"`: Precision
    - `"recall"`: Recall
    - `"f1"`: F1-Score
    - `"roc_auc"`: Area Under ROC Curve (AUROC)
    - `"matthews_corrcoef"`: Matthews Correlation Coefficient (MCC)
  - *Default:* `["accuracy", "roc_auc"]`

- **`refit`**: The metric used to refit the best model after hyperparameter tuning.
  - *Default:* `"accuracy"`

- **`num_jobs`**: The number of CPU cores used for training and hyperparameter search.
  - Set to `k` to use `k` CPU cores, `-1` for all CPU cores, `-k` for all but `k` CPU cores.
  - *Default:* `1`

- **`pre_dispatch`**: Controls job pre-dispatching for parallel execution.
  - *Default:* `"2*n_jobs"`

- **`verbose`**: Controls verbosity of training output.
  - *Default:* `0`

- **`random_state`**: Seed for random number generators for reproducibility.
  - *Default:* `None`

[Back to the main tutorial](https://pykale.github.io/mmai-tutorials/tutorials/brain-disorder-diagnosis/tutorial.html#baseline-and-proposed-model)
