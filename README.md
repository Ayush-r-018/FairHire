![Python](https://img.shields.io/badge/Python-3.13-blue)

![Status](<https://img.shields.io/badge/Status-In%20Progress-yellow>)

![License](https://img.shields.io/badge/License-Educational-green)

---

# FairHire

A custom Machine Learning-based Resume Screening and Candidate Recommendation System developed as a Minor Project.

---

## Project Overview

FairHire Custom ML is an AI-powered recruitment system that predicts whether a candidate should be **Selected** or **Rejected** based on resume and job description information.

Unlike the previous version that relied on pretrained language models, this project focuses on building and training a **custom machine learning model** from scratch using traditional Natural Language Processing (NLP) techniques.

---

## Project Objectives

- Build a custom resume screening model
- Preprocess and clean resume/job description text
- Convert text into numerical features using TF-IDF
- Train multiple Machine Learning models
- Compare model performance
- Select the best-performing model
- Ensure transparency and fairness in hiring decisions

---

## Project Structure

```text
FairHire/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_loading.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_training.ipynb
│   └── 05_model_evaluation.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── utils.py
│   └── __init__.py
│
├── models/
├── outputs/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Dataset Information

### Job Dataset

- Total Records: 1,068
- Features: 7

### Resume Dataset

- Total Records: 10,174
- Features: 5

Target Variable:

- Decision
  - Select
  - Reject

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git & GitHub

---

## Development Progress

### Completed

- [X] Project Setup
- [X] Virtual Environment
- [X] GitHub Repository
- [X] Notebook 01 – Data Loading & Exploration

### In Progress

- [ ] Notebook 02 – Data Preprocessing

### Upcoming

- [ ] Feature Engineering
- [ ] Model Training
- [ ] Model Evaluation
- [ ] Model Comparison
- [ ] Model Saving

---

## Future Enhancements

- Explainable AI (SHAP/LIME)
- Streamlit Web Application
- Resume Ranking Dashboard
- Bias Detection Module
- REST API Deployment

---

## Authors

- Ayush Rauniyar
- Anubhav Jha
- Anshu Shah
- Dipak Kumar Mandal

---

## License

This project is developed for educational and research purposes.
