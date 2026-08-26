# 🩺 Diabetes Prediction using Logistic Regression

An end-to-end machine learning project that predicts whether a patient
is likely to have diabetes using Logistic Regression.

The project covers data exploration, preprocessing, leakage-safe model
training, evaluation, feature interpretation, model serialization,
Streamlit deployment, GitHub version control, and cloud deployment.

## 🚀 Live Demo

[Try the Diabetes Prediction App](https://diabetes-prediction-7t9ljnm4e5gjkc2qnr9aum.streamlit.app/)

## 📌 Project Workflow

Dataset
→ EDA
→ Data Preprocessing
→ Train/Test Split
→ Leakage-Safe Pipeline
→ Logistic Regression
→ Model Evaluation
→ Feature Interpretation
→ Model Serialization
→ Streamlit
→ GitHub
→ Streamlit Cloud

## 📂 Dataset

The dataset contains 768 observations and 9 columns.

The target variable is `Outcome`:

- `0` → No diabetes
- `1` → Diabetes

### Features

| Feature | Description |
|---|---|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Triceps skin fold thickness |
| Insulin | 2-Hour serum insulin |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Diabetes pedigree function |
| Age | Patient age |
| Outcome | Diabetes outcome |

## 🔍 Exploratory Data Analysis

The following analyses were performed:

- Dataset shape and structure
- Data types
- Summary statistics
- Missing-value investigation
- Duplicate-value check
- Target distribution
- Histograms
- Box plots
- Correlation analysis
- Feature distributions and skewness

### Key EDA Findings

- The dataset contains 768 observations.
- There are 500 observations with `Outcome = 0`.
- There are 268 observations with `Outcome = 1`.
- The target distribution is approximately 65% / 35%.
- Glucose showed the strongest relationship with the target.
- Insulin showed a strong right-skewed distribution.
- Several features contained zero values that required careful treatment.

## 🛠️ Data Preprocessing

The following preprocessing steps were performed:

- Train-test split using an 80/20 ratio.
- Zero values representing missing measurements were handled where appropriate.
- Missing numerical values were imputed using training-data statistics.
- Numerical features were scaled.
- Preprocessing was performed using a Scikit-learn Pipeline to prevent data leakage.

## 🤖 Model

A Logistic Regression classifier was trained to predict the binary target variable `Outcome`.

The trained preprocessing and model pipeline was saved using `joblib`.

Model file:

`diabetes_logistic_pipeline.pkl`

## 📊 Model Performance

| Metric | Score |
|---|---:|
| Accuracy | 70.78% |
| ROC-AUC | 81.30% |

Additional evaluation metrics were also calculated:

- Precision
- Recall
- F1-score
- Confusion Matrix
- ROC Curve

## 📈 Feature Interpretation

The Logistic Regression coefficients were interpreted to understand
which features contributed to the prediction.

The strongest positive coefficients were:

- Glucose
- BMI
- Pregnancies
- DiabetesPedigreeFunction
- Age

A positive coefficient indicates that, holding other features constant,
an increase in that feature is associated with a higher model score for
`Outcome = 1`.

## 🌐 Streamlit Deployment

The trained pipeline was integrated into a Streamlit application.

The application allows users to enter patient information and receive:

- Predicted diabetes outcome
- Probability of diabetes

The application was deployed using Streamlit Community Cloud.

## 📁 Project Structure

```text
Diabetes-Prediction/
│
├── diabetesapp.py
├── diabetes_logistic_pipeline.pkl
├── requirements.txt
├── README.md
└── .gitignore
