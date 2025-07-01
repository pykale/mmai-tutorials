# Introduction

## Open Biomedical Multimodal AI Research Workshop

**EMBC 2025 Workshop: Open Biomedical Multimodal AI Research – From Pixels to Molecules – 16 July | Copenhagen, Denmark**

This workshop offers practical, hands-on tutorials in **open biomedical multimodal AI research**, introducing machine learning techniques for leveraging multimodal data in biomedical applications. It focuses on two main goals:

1. Building foundational knowledge and skills in multimodal AI.
2. Fostering open research practices to promote reproducible, reusable, and reliable AI.

---

**Expected Outcomes**

- Explore approaches of leveraging multimodal data in biomedical AI research
- Gain hands-on experience with open-source tools and public datasets
- Learn reproducible and reusable machine learning workflows for multiple biomedical modalities

---

[//]: # (**Target Audience and Prerequisites**)

[//]: # ()
[//]: # (This tutorial is designed for researchers, students, and practitioners in biomedical engineering, healthcare AI, and related fields who:)

[//]: # ()
[//]: # (- Have basic proficiency in Python programming)

[//]: # (- Are familiar with Google Colaboratory &#40;or willing to learn&#41;)

[//]: # (- Are interested in multimodal AI and open, reproducible research)

[//]: # (- Can bring a laptop with internet access to participate fully)
[//]: # ()
[//]: # (---)

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


[//]: # (### Resources Provided)

[//]: # (- All notebooks and data access links)

[//]: # (- PyKale documentation and example pipelines)

[//]: # (- Open discussion forum for continued collaboration)

[//]: # ()
[//]: # (### Structure)


[//]: # ()
[//]: # (### Part 1: Foundational Tutorials with Practical Examples)

[//]: # (This session introduces key concepts in multimodal AI and open research, followed by four focused, hands-on tutorials using **public biomedical datasets** and the **PyKale multimodal AI library**. Each tutorial follows a common pipeline:)

[//]: # ()
[//]: # ()
[//]: # ()
[//]: # ()
[//]: # ()
[//]: # (All tutorials run in **Google Colaboratory** and are designed for **ease of reproducibility and extension**.)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (### Part 2: Group Work)

[//]: # (Participants will form small groups and select **one of the four domains** &#40;Brain, Heart, Cancer, or Drug&#41; to explore deeper:)

[//]: # ()
[//]: # (- Identify specific challenges &#40;e.g., data integration, model generalisation, interpretability&#41;)

[//]: # (- Extend existing tutorial pipelines or propose alternative solutions)

[//]: # (- Present findings and ideas to the group for discussion)

[//]: # ()
[//]: # (Facilitators and demonstrators will provide support throughout, encouraging **open sharing, creativity, and peer learning**.)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (This tutorial forms a **launchpad for open, collaborative, and impactful biomedical AI research**, aligning with the broader vision of EMBC and the global scientific community.)

[//]: # ()

## Contributors

This workshop is made possible by contributions from:

- **[Shuo Zhou](https://github.com/shuo-zhou)**
- **[Xianyuan Liu](https://github.com/xianyuanliu)**
- **[L. M. Riza Rizky](https://github.com/zaRizk7)**
- **[Mohammod Naimul Islam Suvon](https://github.com/Mdnaimulislam)**
- **[Kelly Ding](https://github.com/kellydingzx)**
- **[Peter Charlton](https://github.com/peterhcharlton)**
- **[Wenrui Fan](https://github.com/orgs/Shef-AIRE/people/wenruifan)**
- **[Sina Tabakhi](https://github.com/SinaTabakhi)**
- **[Jiayang Zhang](https://github.com/jiayang-zhang)**
- **[Haiping Lu](https://github.com/haipinglu)**

<!-- ```{tableofcontents}
``` -->
