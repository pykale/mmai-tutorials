# Extension Tasks

## Task 1 Explore the Effect of Domain Adaptation

Turn off domain adaptation by updating the config file and re-running training and testing.

Replace `configs/DA_cross_domain.yaml` with `configs/non_DA_cross_domain.yaml` in the Configuration section of [Step 0](https://pykale.github.io/mmai-tutorials/tutorials/drug-target-interaction/tutorial-drug.html#step-0-environment-preparation) as shown below.

```python
cfg.merge_from_file("configs/non_DA_cross_domain.yaml")
```

>Tip: Compare the results with and without domain adaptation to see how it affects model performance.

## Task 2 Evaluate DrugBAN on BindingDB Dataset

To use the BindingDB dataset, modify the relevant line in the Configuration section of [Step 0](https://pykale.github.io/mmai-tutorials/tutorials/drug-target-interaction/tutorial-drug.html#step-0-environment-preparation) as shown below.

```python
cfg.DATA.DATASET = "bindingdb"
```

Reload the dataset and re-run training and testing.

> Tip: See if the model struggles more or less with the new dataset. It can reveal how generalisable DrugBAN is.
