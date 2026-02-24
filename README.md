# 🏥 Healthcare Insurance Premium Prediction (End-to-End ML Project)

## 📌 Overview

This project predicts **health insurance premium cost** based on demographic details, lifestyle habits, and medical history.
Users can enter their information through an interactive **Streamlit web application**, and the trained Machine Learning model estimates the expected insurance premium.

The project demonstrates a **complete end-to-end Machine Learning workflow**, including EDA, preprocessing, model building, deployment, and debugging real-world issues.

> ✅ Developed as part of academic learning and enhanced with additional debugging and deployment improvements.

---

## 🎯 Objective

Insurance premium pricing depends on multiple risk factors such as:

* Age
* BMI category
* Medical history
* Smoking habits
* Income level
* Employment status
* Genetic risk

The objective of this project is to build a predictive model that accurately estimates insurance premiums using these features.

---

## 🧠 Project Workflow

### 🔹 1. Exploratory Data Analysis (EDA) – Jupyter Notebook

* Data understanding and visualization
* Handling missing values
* Outlier detection and treatment
* Feature relationship analysis

### 🔹 2. Data Preprocessing

* Data cleaning
* Label encoding & One-hot encoding
* Feature engineering
* Feature scaling
* Handling categorical variables

### 🔹 3. Model Building

* Trained regression models for premium prediction
* Implemented **two separate models**:

  * Model for younger individuals (Age < 25)
  * Model for others (Age ≥ 25)
* Saved trained models and scalers using Joblib

### 🔹 4. Backend Implementation – VS Code

* Built preprocessing pipeline
* Implemented scaling logic
* Created reusable prediction helper functions
* Ensured training–inference feature consistency

### 🔹 5. Deployment – Streamlit Cloud

* Developed interactive Streamlit UI
* Deployed ML application to Streamlit Cloud
* Resolved deployment challenges:

  * Feature mismatch during inference
  * Dependency version conflicts
  * Streamlit compatibility with Python environment

---

## 🚀 Key Features

✔ Interactive Streamlit UI
✔ End-to-end ML pipeline implementation
✔ Separate models for improved prediction accuracy
✔ Real-time insurance premium prediction
✔ Production-style preprocessing logic
✔ Deployment debugging and troubleshooting experience

---

## 🛠 Tech Stack

* Python
* Pandas & NumPy
* Scikit-learn
* XGBoost
* Streamlit
* Joblib
* Git & GitHub

---

## 📂 Project Structure

```
├── notebooks/              # EDA & experimentation
├── artifacts/              # Saved models & scalers
├── main.py                 # Streamlit UI
├── prediction_helper.py    # Preprocessing & prediction logic
├── requirements.txt        # Dependencies
└── README.md
```

---

## 🌐 Live Application

👉 https://healthcare-ml-project.streamlit.app/

---

## 📚 Learning Outcomes

* End-to-end ML project development
* Data preprocessing and feature engineering
* Model comparison and selection
* Handling inference feature mismatch
* Deployment on Streamlit Cloud
* Debugging dependency and environment issues

---

## 👨‍💻 Author

**Dhruva Jilloju**

B.Tech Mechanical Engineering (2024)

Aspiring Data Analyst / Data Scientist
