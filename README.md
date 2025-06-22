
# 🏠 House Price Prediction using Regression

![GitHub last commit](https://img.shields.io/github/last-commit/PranavKrSingh/House-Price-Prediction-using-Regression)
![GitHub repo size](https://img.shields.io/github/repo-size/PranavKrSingh/House-Price-Prediction-using-Regression)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

This project builds a machine learning model to predict house sale prices using various features from the Ames Housing Dataset. It follows a complete pipeline: from data preprocessing and exploratory analysis to model training, evaluation, and prediction.

---

## 📸 Screenshots

| EDA Visualizations | Model Output |
|--------------------|--------------|
| ![EDA](notebooks/screenshots/eda_heatmap.png) | ![Prediction](notebooks/screenshots/prediction_sample.png) |

> *(Add these screenshots manually under `notebooks/screenshots/` folder to enable rendering)*

---

## 📂 Project Structure

```

house-price-prediction/
│
├── data/
│   └── raw/
│       ├── train.csv
│       ├── test.csv
│       └── data\_description.txt
│
├── notebooks/
│   └── EDA.ipynb              # Exploratory Data Analysis
│
├── src/
│   ├── data\_preprocessing.py  # Missing value handling & encoding
│   ├── feature\_engineering.py # New features
│   ├── model\_training.py      # Model training and evaluation
│   ├── predict.py             # Predict on new data
│   └── utils.py               # Utility functions
│
├── requirements.txt
├── .gitignore
└── README.md

````

---

## 🚀 Quick Start

1. **Clone the repository**
    ```bash
    git clone https://github.com/PranavKrSingh/House-Price-Prediction-using-Regression.git
    cd House-Price-Prediction-using-Regression
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Train the model**
    ```bash
    python src/model_training.py
    ```

4. **Run EDA notebook**
    ```bash
    jupyter notebook notebooks/EDA.ipynb
    ```

---

## 📊 About the Dataset

- **Train.csv**: 1460 records with 81 features (including `SalePrice`)
- **Test.csv**: 1459 records with 80 features (no `SalePrice`)
- Categorical + Numerical features

---

## 📈 Machine Learning Approach

- **Model**: Random Forest Regressor
- **Target**: `SalePrice` (continuous) → **regression problem**
- **Evaluation**: 5-Fold Cross-Validation using RMSE

---

## 🔧 Tools & Libraries Used

- Python 3.10+
- pandas, numpy
- seaborn, matplotlib
- scikit-learn
- Jupyter Notebook

---

## 🧠 Why Regression?

This problem involves predicting a **continuous numeric value** (house price), not classifying categories — which makes it a regression problem rather than classification.

---

## 📝 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and share.

---

## 🔗 Connect with Me

- GitHub: [@PranavKrSingh](https://github.com/PranavKrSingh)
- LinkedIn: [Pranav Kumar Singh](https://linkedin.com/in/pranavkumarsingh32)
