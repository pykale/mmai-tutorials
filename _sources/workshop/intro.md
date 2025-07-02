# Introduction

## Welcome

### Open Biomedical Multimodal AI Research Workshop

<!-- **EMBC 2025 Workshop: Open Biomedical Multimodal AI Research – From Pixels to Molecules – 16 July | Copenhagen, Denmark** -->

This workshop offers practical, hands-on tutorials in **open biomedical multimodal AI research**, introducing machine learning techniques for leveraging multimodal data in biomedical applications. It brings together three core themes:

1. **Foundational skills in multimodal learning**: Developing knowledge and practical skills in leveraging multimodal data, including fusion, regularization, and interaction techniques for biomedical research.
2. **Open research**: Enabling impactful and high-quality research through open-access data and code. All tutorials used in this workshop are openly available in the [GitHub repository](https://github.com/pykale/mmai-tutorials).
3. **Reproducible pipelines with PyKale**: Promoting open research practices using `PyKale`, which supports standardized machine learning pipelines and configurable experimentation without extra coding—making AI research more reproducible, reusable, and recyclable.

---

### Questions to Consider

Consider the following questions to help familiarize yourself with the key concepts of this workshop:

- Have you used publicly available data or code in your work?

- Have you ever shared data or code from your own research?

- Have you practiced reproducible research methods?

Consider the following questions, choose those that apply to you, to reflect on your experience:

- Which multimodal AI applications are you most interested in?
- What aspects of the tutorials did you find most helpful or challenging?
- How do you envision multimodal AI contributing to your own research?
- What challenges do you currently face when working with multimodal data or methods?
- Are there any tools or techniques present in the tutorials that you found particularly useful or innovative?
- Are there any specific tools or features you wish our AI Research Engineering team would develop to support your work?

### Discussion forum for Q&A etc

We have a [discussion forum](https://github.com/pykale/mmai-tutorials/discussions) as our primary communication channel, e.g. for Q&A, information sharing, and discussion. Please ask questions or post information there, rather than emailing the organisers directly. This will help others to benefit from the answers and help build an engaging community. You will need a [GitHub account](https://github.com/join) to post questions.

---

## Overview of the Materials

This workshop covers the tutorials for **four biomedical applications** using the **[PyKale multimodal AI library](https://github.com/pykale/pykale)**. You are welcome to focus on one application with exploration tasks or explore all four applications.

**Tutorial Topics:**

1. **Brain Disorder Diagnosis**
   - **Data**: ABIDE (Autism Brain Imaging Data Exchange)
   - **Goal**: Use neuroimaging and phenotypic data for autism classification

2. **Cardiovascular Disease Assessment**
   - **Data**: MIMIC Chest X-rays and ECG signals
   - **Goal**: Integrate imaging and physiological signals for risk prediction

3. **Cancer Classification**
   - **Data**: TCGA (The Cancer Genome Atlas)
   - **Goal**: Combine genomics and transcriptomics data for cancer subtype classification

4. **Drug–Target Interaction Prediction**
   - **Data**: BindingDB and BioSNAP
   - **Goal**: Predict molecular interactions from structural and textual features

The tutorial materials are organized into a Jupyter Book comprising four chapters. Each chapter is prepared in an accessible and executable Jupyter notebook corresponds to a specific biomedical application. You’ll find a rocket icon <i class="fas fa-rocket"></i> near the top mid-right of each executable page. We recommend first reviewing the content in your browser (HTML format), then launching the corresponding notebook, preferably in Google Colab, by clicking the rocket icon (via <i class="fas fa-rocket"></i>) to run and experiment with the code.

The tutorials are organized as standardized file structure, which is shown below:

```text
    ├───tutorial.ipynb
    ├───config.py
    ├───configs
    │   ├───base.yml
    │   ├───**.yml
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
