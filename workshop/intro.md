# Introduction

## Welcome

### Open Biomedical Multimodal AI Research

**Workshop@EMBC-2025  | 2:30 PM, 16 July | B3 M7-8, Bella Center, Copenhagen, Denmark**

This workshop offers practical, hands-on tutorials in **open biomedical multimodal AI research**,
introducing machine learning techniques for leveraging multimodal data in biomedical applications.
It brings together three core themes:

1. **Skills in multimodal learning**: Developing knowledge and practical skills in multimodal AI for biomedical applications. Specifically, **regularization**, **fusion (intermediate and late)**, and **interaction**, to leverage multimodal data are covered in the tutorials.
2. **Open research**: Enabling impactful and high-quality research through open-access data and code. All tutorials used in this workshop are openly available in the [GitHub repository](https://github.com/pykale/mmai-tutorials).
3. **Reproducible pipelines with PyKale**: The core machine learning library behind the tutorial of this workshop is [`PyKale`](https://github.com/pykale/pykale), which supports standardized machine learning pipelines and configurable experimentation without extra coding—making AI research more reproducible, reusable, and recyclable.

---

## Overview of the Materials

This workshop covers tutorials on **four biomedical applications** using the **[PyKale multimodal AI library](https://github.com/pykale/pykale)**.
You are welcome to focus on one application with its exploration tasks or explore all four applications.
The [workshop slides](https://www.linkedin.com/posts/ukomain_embc-2025-slides-activity-7353336771377602563-FNjK?utm_source=share&utm_medium=member_desktop&rcm=ACoAACntBqIB-Um3rPdeWmJTIdKxPHAoiWH7JYc) introduce multimodal AI and PyKale and provide summaries of each tutorial.

**Tutorial Topics:**

1. **Brain Disorder Diagnosis**

   - **Modalities**: Neuroimaging (fMRI) and phenotypic features (e.g., age, gender, IQ)
   - **Task**: Use neuroimaging and phenotypic data for autism classification
   - **Multimodal approach**: Regularization - using phenotypic features to regularize feature embedding for reducing the phenotypic effect (e.g. site effect) in neuroimaging data to improve cross-site classification performance
   - **Dataset**: [ABIDE (Autism Brain Imaging Data Exchange)](https://fcon_1000.projects.nitrc.org/indi/abide/)

2. **Cardiovascular Disease Assessment**

   - **Modalities**: Chest X-ray images and ECG signals
   - **Task**: Integrate imaging and physiological signals for classifying health and cardiothoracic abnormalities
   - **Multimodal approach**: Intermediate fusion - combining CXR and ECG at feature embedding level
   - **Dataset**: MIMIC [Chest X-rays](https://physionet.org/content/mimic-cxr/2.1.0/) and [ECG signals](https://physionet.org/content/mimic-iv-ecg/1.0/)

3. **Cancer Classification**

   - **Modalities**: DNA methylation, mRNA expression, and miRNA expression.
   - **Task**: Combine genomics and transcriptomics data for cancer classification
   - **Multimodal approach**: Late fusion - contrcuting cross-omics tensor for probability fusion
   - **Dataset**: [TCGA (The Cancer Genome Atlas)](https://www.cancerimagingarchive.net/collection/tcga-brca/)

4. **Drug–Target Interaction Prediction**

   - **Modalities**: Protein structures (3D) and molecular graphs (SMILES)
   - **Task**: Predict molecular interactions from structural and textual features
   - **Multimodal approach**: Interaction - bilinear interaction between protein and molecular embedding
   - **Dataset**: [BindingDB](https://www.bindingdb.org/rwd/bind/index.jsp) and [BioSNAP](https://snap.stanford.edu/biodata/)

The core functions of each tutorial are implemented in the [`PyKale` APIs](https://pykale.readthedocs.io/en/latest/) of a **standardized machine learning pipeline**:

> **Data loading → Preprocessing → Embedding → Prediction → Evaluation → Interpretation**

### Discussion forum for Q&A etc

We have a [discussion forum](https://github.com/pykale/mmai-tutorials/discussions) as our primary communication channel, e.g. for Q&A, information sharing, and discussion. Please ask questions or post information there, rather than emailing the organisers directly. This will help others to benefit from the answers and help build an engaging community. You will need a [GitHub account](https://github.com/join) to post questions.

### Questions to Consider

#### Before We Begin

_Consider the following questions to help familiarize yourself with the key concepts of this workshop:_

- Have you used publicly available data or code in your work?
- Have you ever shared data or code from your own research?
- Have you applied any practices to make your research more reproducible?
- Do you currently face any challenges when working with multimodal data or methods?

#### Post-Tutorial Reflection

_Consider the following questions, choose those that apply to you, to reflect on your experience:_

- Were there any tools or techniques introduced in the tutorials that you found particularly useful or innovative?
- Which aspects of the tutorials did you find most helpful, and which were most challenging?
- How do you see multimodal AI contributing to or shaping your own research going forward?
