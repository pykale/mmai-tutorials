# Introduction

## Welcome

### Open Biomedical Multimodal AI Research Workshop

This workshop offers practical, hands-on tutorials in **open biomedical multimodal AI research**, introducing machine learning techniques for leveraging multimodal data in biomedical applications. It brings together three core themes:

1. **Foundational skills in multimodal learning**: Developing knowledge and practical skills in multimodal AI for biomedical applications. Specifically, three approaches, **regularization**, **hybrid fusion**, and **interaction**, to leverage multimodal data are covered in the tutorials.
2. **Open research**: Enabling impactful and high-quality research through open-access data and code. All tutorials used in this workshop are openly available in the [GitHub repository](https://github.com/pykale/mmai-tutorials).
3. **Reproducible pipelines with PyKale**: The core machine learning library behind the tutorial of this workshop is [`PyKale`](https://github.com/pykale/pykale), which supports standardized machine learning pipelines and configurable experimentation without extra coding—making AI research more reproducible, reusable, and recyclable.

In person event: **EMBC 2025 Workshop: Open Biomedical Multimodal AI Research – From Pixels to Molecules – 2:30 PM 16 July | B3 M7-8 of Bella Center, Copenhagen, Denmark**.

---

## Overview of the Materials

This workshop covers the tutorials for **four biomedical applications** using the **[PyKale multimodal AI library](https://github.com/pykale/pykale)**. You are welcome to focus on one application with exploration tasks or explore all four applications.

**Tutorial Topics:**

1. **Brain Disorder Diagnosis**
   - **Dataset**: [ABIDE (Autism Brain Imaging Data Exchange)](https://fcon_1000.projects.nitrc.org/indi/abide/)
   - **Modalities**: Neuroimaging (fMRI) and phenotypic features (e.g., age, gender, IQ)
   - **Task**: Use neuroimaging and phenotypic data for autism classification
   - **Multimodal approach**: Regularization - using phenotypic features to regularize feature embedding for reducing the phenotypic effect (e.g. site effect) in neuroimaging data to improve cross-site classification performance.
   
2. **Cardiovascular Disease Assessment**
   - **Dataset**: MIMIC [Chest X-rays]((https://physionet.org/content/mimic-cxr/2.1.0/)) and [ECG signals](https://physionet.org/content/mimic-iv-ecg/1.0/)
   - **Modalities**: Chest X-ray images and ECG signals
   - **Task**: Integrate imaging and physiological signals for classifying health and cardiothoracic abnormalities
   - **Multimodal approach**: Hybrid fusion - combining CXR and ECG at feature and decision level for improved classification.

3. **Cancer Classification**
   - **Dataset**: [TCGA (The Cancer Genome Atlas)]((https://www.cancerimagingarchive.net/collection/tcga-brca/))
   - **Modalities**: DNA methylation, mRNA expression, and miRNA expression.
   - **Task**: Combine genomics and transcriptomics data for cancer classification
   - **Multimodal approach**: Late fusion - cross-omics tensor for probability fusion.

4. **Drug–Target Interaction Prediction**
   - **Dataset**: [BindingDB](https://www.bindingdb.org/rwd/bind/index.jsp) and [BioSNAP](https://snap.stanford.edu/biodata/)
   - **Modalities**: Protein structures (3D) and molecular graphs (SMILES)
   - **Task**: Predict molecular interactions from structural and textual features
   - **Multimodal approach**: Interaction - bilinear interaction between protein and molecular embedding.

The tutorial materials are organized into a Jupyter Book comprising four chapters. Each chapter is prepared in an accessible and executable Jupyter notebook corresponds to a specific biomedical application. You’ll find a rocket icon <i class="fas fa-rocket"></i> near the top mid-right of each executable page. We recommend first reviewing the content in your browser (HTML format), then launching the corresponding notebook, preferably in Google Colab, by clicking the rocket icon (via <i class="fas fa-rocket"></i>) to run and experiment with the code.

The tutorials are organized as standardized file structure. The common file structure of a tutorial is shown below:

```text
    ├───tutorial.ipynb
    ├───config.py
    ├───configs
    │   ├───base.yml
    │   ├───**.yml
```

Some tutorials may also include additional resources. A more comprehensive file structure is shown below:

```text
    ├───tutorial.ipynb
    ├───config.py
    ├───configs
    │   ├───base.yml
    │   ├───**.yml
    |───extend-reading
    │   ├───**.md
    ├───model.py
    ├───models
    │   ├───**.pt
    ├───data
    │   ├───**.csv
    │   ├───**.**
    ├───images
    │   ├───**.png
    │   ├───**.jpg
    ├───**.py
```

Each tutorial follows standardized machine learning pipelines:

> **Data loading → Preprocessing → Embedding → Prediction → Evaluation → Interpretation**

### Configuration

As shown in the file structure above, each tutorial has a `config.py` script that defines the base configuration settings. These settings can be customized or overridden using external `.yml` files located in the `configs` directory. The configuration system allows for easy parameter tuning and reproducibility across different runs of the tutorials.

Using a configuration file offers several benefits:

- **Separation of concerns**: Keeps the notebook focused on analysis and results, while experiment parameters are managed externally.
- **Reproducibility**: Ensures that all experiment settings are recorded, making it easier to reproduce results consistently.
- **Flexibility**: Allows rapid switching between different configurations without modifying the core implementation.
- **Scalability**: Facilitates managing multiple experiments systematically, especially in larger workflows or batch processing.

Please refer to the provided configuration files for details on how to customize your experiment.

### Discussion forum for Q&A etc

We have a [discussion forum](https://github.com/pykale/mmai-tutorials/discussions) as our primary communication channel, e.g. for Q&A, information sharing, and discussion. Please ask questions or post information there, rather than emailing the organisers directly. This will help others to benefit from the answers and help build an engaging community. You will need a [GitHub account](https://github.com/join) to post questions.

### Questions to Consider

Consider the following questions to help familiarize yourself with the key concepts of this workshop:

- Have you used publicly available data or code in your work?

- Have you ever shared data or code from your own research?

- Have you practised reproducible research methods?

Consider the following questions, choose those that apply to you, to reflect on your experience:

- Are there any tools or techniques present in the tutorials that you found particularly useful or innovative?
- What aspects of the tutorials did you find most helpful or challenging?
- How do you envision multimodal AI contributing to your own research?
- What challenges do you currently face when working with multimodal data or methods?
