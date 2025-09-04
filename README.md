
# 📰 Fake News Detection System

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-0.24.2-orange?style=for-the-badge&logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-1.26.0-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

An end-to-end Machine Learning project that classifies news articles as Real or Fake using Natural Language Processing (TF-IDF) and Scikit-learn, deployed as an interactive Streamlit web app.

***

## 🚀 Live Demo



*You can view and interact with the live application here: https://akashwav-fake-news-detector.streamlit.app/*

***

## 📖 Table of Contents

* [About The Project](#about-the-project)
* [Key Features](#-key-features)
* [Technology Stack](#-technology-stack)
* [Project Structure](#-project-structure)
* [Setup and Installation](#-setup-and-installation)
* [Usage](#-usage)
* [Methodology Overview](#-methodology-overview)
* [Model Performance](#-model-performance)
* [License](#-license)
* [Acknowledgements](#-acknowledgements)

***

## 🎯 About The Project

In the age of digital information, the rapid spread of fake news poses a significant threat to public discourse and societal trust. This project aims to combat this issue by leveraging Natural Language Processing (NLP) and Machine Learning to build an automated detection system.

The system is trained on a dataset of over 44,000 news articles and uses a scikit-learn pipeline to process text and make predictions. The final model is wrapped in a user-friendly web interface built with Streamlit, allowing anyone to classify an article's text in real-time.

***

## ✨ Key Features

* **Text Preprocessing:** A robust NLP pipeline for cleaning, tokenizing, lemmatizing, and removing stopwords.
* **TF-IDF Feature Extraction:** Converts unstructured text into meaningful numerical vectors.
* **High-Accuracy Classification:** Utilizes a Logistic Regression model achieving ~99% accuracy on the test set.
* **Interactive Web Interface:** A simple and intuitive UI for users to paste text and receive instant predictions.
* **Cloud Deployment:** Hosted on Streamlit Community Cloud for public access and demonstration.

***

## 🛠️ Technology Stack

This project was built using the following technologies and libraries:

* **Language:** Python 3.10+
* **Core ML/DS Libraries:**
    * [Scikit-learn](https://scikit-learn.org/): For the ML pipeline, models, and feature extraction.
    * [Pandas](https://pandas.pydata.org/): For data manipulation and analysis.
    * [NumPy](https://numpy.org/): For numerical operations.
* **NLP Libraries:**
    * [NLTK](https://www.nltk.org/): For tokenization and stopwords.
    * [spaCy](https://spacy.io/): For high-performance lemmatization.
* **Web Framework:**
    * [Streamlit](https://streamlit.io/): For building the interactive web application.
* **Version Control & Deployment:**
    * Git & [GitHub](https://github.com/): For version control.
    * [Git LFS](https://git-lfs.com/): For versioning large data files.
    * [Streamlit Community Cloud](https://streamlit.io/cloud): For hosting the application.

***

## 📁 Project Structure

The repository is organized with a clear separation of data, source code, notebooks, and models to ensure reproducibility.

```

├── data/
│   ├── raw/         \# Raw dataset files (Fake.csv, True.csv)
│   └── ...
├── models/          \# Saved model files (.joblib)
├── notebooks/       \# Jupyter notebooks for EDA and modeling
├── reports/         \# Final project report and figures
├── src/             \# Source code for the application (app.py)
├── .gitignore       \# Specifies files for Git to ignore
├── README.md        \# This file
└── requirements.txt \# Project dependencies

````

***

## ⚙️ Setup and Installation

Follow these steps to set up and run the project locally.

### 1. Prerequisites
Ensure you have Git and Python 3.10+ installed on your system.

### 2. Clone the Repository
Clone this repository to your local machine. If you haven't set up Git LFS, you may need to install it (`git lfs install`).
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
````

### 3\. Set Up the Data (Important)

The raw dataset is tracked by Git LFS. When you clone the repository, Git should automatically download the large data files. If the `data/raw/` folder is empty after cloning, run this command to pull the data:

```bash
git lfs pull
```

### 4\. Create a Virtual Environment and Install Dependencies

It is highly recommended to use a virtual environment.

```bash
# Create a virtual environment
python -m venv .venv

# Activate it
# On Windows: .venv\Scripts\activate
# On macOS/Linux: source .venv/bin/activate

# Install the required packages
pip install -r requirements.txt
```

### 5\. Download NLP Models

The application requires specific data packages from NLTK and spaCy.

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
python -m spacy download en_core_web_sm
```

-----

## ▶️ Usage

To run the Streamlit application locally, execute the following command in your terminal from the project's root directory:

```bash
streamlit run src/app.py
```

Your web browser will automatically open to the application's local URL.

-----

## 🔬 Methodology Overview

The project follows a standard machine learning workflow:

1.  **Data Cleaning:** The raw text is normalized (lowercase, remove punctuation/URLs).
2.  **Preprocessing:** Text is tokenized, stopwords are removed, and words are lemmatized to their root form.
3.  **Feature Engineering:** The cleaned text is converted into a high-dimensional vector space using TF-IDF.
4.  **Modeling:** A Logistic Regression model is trained on the vectorized data to learn the patterns that distinguish real from fake news.
5.  **Evaluation:** The model is evaluated on a held-out test set to ensure its performance and ability to generalize.

-----

## 📊 Model Performance

The final Logistic Regression model achieved **\~99% accuracy** on the test set, demonstrating a high level of proficiency in correctly classifying unseen news articles. Detailed metrics (Precision, Recall, F1-Score) can be found in the final project report.

-----

## 📄 License

This project is distributed under the MIT License. See `LICENSE` for more information.

-----

<!-- end list -->

```
```