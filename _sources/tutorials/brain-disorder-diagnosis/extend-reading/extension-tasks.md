# Extended Exploration

For those eager to explore further or just curious to tweak configurations to enhance performance, we’ve prepared a set of optional tasks. These tasks are designed to encourage experimentation without requiring significant changes to the core code.

---

## Task 1: Explore Different Atlases and FCs *(20–120+ minutes)*

We provide multiple brain atlases and functional connectivity (FC) embeddings to experiment with. You can create a new configuration file or simply uncomment the `cfg.DATASET.ATLAS` and `cfg.DATASET.FC` options in the configuration section.

**Open-ended questions:**

- Is selecting an appropriate atlas beneficial for building accurate brain disorder diagnosis models?
- If so, how much improvement can we expect from choosing the best atlas?
- Does the best-performing atlas help interpret and localize key ROIs relevant to ASD?
- Or is the choice of atlas less impactful than the choice of functional connectivity method?

---

## Task 2: Better Phenotypes? *(30–60+ minutes)*

Our results show that using only **site labels** already leads to performance improvements. In contrast to Kunda et al. (2022) who used site labels for domain adaptation and treated other phenotypic variables merely as additional features, our implementation in **PyKale** allows for **full integration of all available phenotypic variables** into the domain adaptation process when specified.

This raises a key question: could leveraging **a richer set of phenotypes** beyond site information further enhance multi-site model generalization?

**Questions to explore:**

- Is the **site label alone** truly sufficient for effective multi-site data integration?
- Are there phenotypes with **distinct distributions across sites** that may introduce bias or noise?
- Can incorporating those phenotypes improve performance beyond site-only models?

:::{warning}
Given that there are many missing values as seen previously, this task might be challenging for users who are unfamiliar with Python and `pandas`, as it may require manual crafting for encoding or imputation as done in `preprocess_phenotypic_data`.
:::

---

## Task 3: More Sites → Better Generalization? *(20–60+ minutes)*

With ten sites, domain adaptation shows improved generalization under the **leave-one-group-out (LPGO)** setting. This raises new questions:

**Things to consider:**

- Does domain adaptation continue to help as we include **more sites**, or is the benefit limited to fewer-site scenarios?
- Is there a **saturation point** where adding more sites stops improving generalization, or even worsens it?
- Could fewer but more homogeneous sites be better than many heterogeneous ones?

---

These tasks are designed to help you dive deeper into model robustness, generalizability, and interpretability in real-world neuroimaging settings. Feel free to explore, question, and iterate!

Hope you enjoy this tutorial!

## Exercise Solutions

:::{solution} find-number-of-samples
:class: dropdown
:label: solution-find-number-of-samples

There are 722 samples found. To find the number of samples,
we can use `len(phenotypes)` which will output 722.
:::

:::{solution} find-roi-count
:class: dropdown
:label: solution-find-roi-count

There are 32 ROIs found. To find the number of ROIs,
we can use `len(rois)` which will output 32.
:::

:::{solution} find-number-of-phenotypes
:class: dropdown
:label: solution-find-number-of-phenotypes

Looking at the dataframe, there are 104 phenotypes based on
the number of columns.
:::

:::{solution} find-number-of-phenotypes-after-preprocess
:class: dropdown
:label: solution-find-number-of-phenotypes-after-preprocess

By calling `phenotypes.shape`, we can inspect the number
of rows and columns. We can see that there are 19 encoded
phenotypes.

If we breakdown the encoded phenotypes:

- Two are continuous variables of `AGE_AT_SCAN` and `FIQ`.
- Ten from the encoded `SITE_ID` variable.
- Two from the encoded `SEX` variable.
- Three from the encoded `HANDEDNESS_CATEGORY` variable.
- Two from the encoded `EYE_STATUS_AT_SCAN` variable.

Thus, in total we have 19 encoded phenotypes.
:::

:::{solution} understanding-one-hot-encoding
:class: dropdown
:label: solution-understanding-one-hot-encoding

One-hot encoding essentially maps the categories into a binary vector space where each category is represented by a unique vector with a single high (commonly set to one) value and all other positions set to zero. It will increase the dimension given the number of categories found within a categorical variable.
:::

:::{solution} find-total-models-produced
:class: dropdown
:label: solution-find-total-models-produced

To estimate the total number of models trained:
- SKF: `n * k`, where `n` is the number of repetition and `k` is the fold.
- LPGO: `C(m, p) = m! / (p! * (m - p)!)`, where `m` is the total number of groups and `p` is the number of group left out for testing.

Following this formula we can obtain:
- SKF: `5 * 10 = 50`
- LPGO: `5! / (2! * (5 - 2)!) = 10`
:::

:::{solution} find-the-aggregate-in-cv-results
:class: dropdown
:label: solution-find-the-aggregate-in-cv-results

Some notable examples found in `cv_results_` include:

- `mean_test_<metric>`: The mean performance score of the specified metric across all validation folds.

- `std_test_<metric>`: The standard deviation of the metric across the folds, providing a measure of variability.

- `rank_test_<metric>`: The rank of each hyperparameter configuration based on `mean_test_<metric>`, with lower values indicating better performance.

These entries allow for easy comparison and selection of the best-performing model configuration with different trade-offs, even when having `refit` set to a specific metric.
:::
