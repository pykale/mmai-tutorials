# Introduction

**EMBC 2025 Workshop: Open Biomedical Multimodal AI Research – From Pixels to Molecules – 16 July | Copenhagen, Denmark**

## Overview

This workshop provides a practical and hands-on introduction to **open biomedical multimodal AI research**, empowering participants to apply state-of-the-art machine learning techniques across diverse biomedical data types. The workshop is designed around two main objectives:
1. Building foundational knowledge and skills in multimodal AI using open tools and datasets.
2. Fostering collaborative exploration of real-world challenges in biomedical domains.

---

### Learning Outcomes
By the end of the tutorial, participants will:
- Explore approaches of leveraging multimodal data in biomedical AI research
- Gain hands-on experience with open-source tools and public datasets
- Learn reproducible machine learning workflows for multiple biomedical modalities
- Be equipped to adapt and apply multimodal AI methods in their own research

---

### Target Audience and Prerequisites

This tutorial is designed for researchers, students, and practitioners in biomedical engineering, healthcare AI, and related fields who:

- Have basic proficiency in Python programming
- Are familiar with Google Colaboratory (or willing to learn)
- Are interested in multimodal AI and open, reproducible research
- Can bring a laptop with internet access to participate fully

---

### How to go through the tutorial

The tutorial materials are organized into a Jupyter Book comprising four chapters. Each chapter is prepared in an executable Jupyter notebook corresponds to a specific biomedical application. You’ll find a rocket icon <i class="fas fa-rocket"></i> near the top mid-right of each executable page. We recommend first reviewing the content in your browser (HTML format), then launching the corresponding notebook—preferably in Google Colab—by clicking the rocket icon (via <i class="fas fa-rocket"></i>) to run and experiment with the code.


### Resources Provided
- All notebooks and data access links
- PyKale documentation and example pipelines
- Open discussion forum for continued collaboration

## Structure

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

### Part 1: Foundational Tutorials with Practical Examples
This session introduces key concepts in multimodal AI and open research, followed by four focused, hands-on tutorials using **public biomedical datasets** and the **PyKale multimodal AI library**. Each tutorial follows a common pipeline:

> **Data loading → Preprocessing → Embedding → Prediction → Evaluation → Interpretation**

**Tutorial Topics:**
1. **Brain Disorder Diagnosis**
   - **Data**: ABIDE (Autism Brain Imaging Data Exchange)
   - **Goal**: Use neuroimaging and phenotypic data for autism classification

2. **Cardiovascular Disease Assessment**
   - **Data**: MIMIC Chest X-rays and ECG signals
   - **Goal**: Integrate imaging and physiological signals for risk prediction

3. **Cancer Classification**
   - **Data**: TCGA (The Cancer Genome Atlas)
   - **Goal**: Combine genomics and histopathology for cancer subtype classification

4. **Drug–Target Interaction Prediction**
   - **Data**: BindingDB and BioSNAP
   - **Goal**: Predict molecular interactions from structural and textual features

All tutorials run in **Google Colaboratory** and are designed for **ease of reproducibility and extension**.

---

### Part 2: Group Work
Participants will form small groups and select **one of the four domains** (Brain, Heart, Cancer, or Drug) to explore deeper:

- Identify specific challenges (e.g., data integration, model generalisation, interpretability)
- Extend existing tutorial pipelines or propose alternative solutions
- Present findings and ideas to the group for discussion

Facilitators and demonstrators will provide support throughout, encouraging **open sharing, creativity, and peer learning**.

---

This tutorial forms a **launchpad for open, collaborative, and impactful biomedical AI research**, aligning with the broader vision of EMBC and the global scientific community.


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
