
# 🏠 House Price Prediction using Regression

This project builds a machine learning model to predict house sale prices using various features from the Ames Housing Dataset. It follows a complete pipeline: from data preprocessing and exploratory analysis to model training, evaluation, and prediction.

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

## 📊 Dataset

- **Train.csv**: 1460 records with 81 features (including `SalePrice`).
- **Test.csv**: 1459 records with 80 features (without `SalePrice`).
- Dataset contains both numerical and categorical features.

## ✅ Features Handled
- Categorical and numerical variable processing
- Missing value imputation
- Feature Engineering (e.g., Total SF)
- One-hot encoding for categorical data

## 🧠 Model Used

- **Random Forest Regressor** from Scikit-Learn
- Evaluated using **5-Fold Cross-Validation** with **RMSE**

## 📝 Steps to Run

1. Clone the repo:
    ```bash
    git clone https://github.com/PranavKrSingh/House-Price-Prediction-using-Regression.git
    cd House-Price-Prediction-using-Regression
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run model training:
    ```bash
    python src/model_training.py
    ```

4. Check `submission.csv` for predictions.

5. For EDA, open:
    ```bash
    jupyter notebook notebooks/EDA.ipynb
    ```

## 📦 Output

- Trained model with cross-validation score
- Final predictions saved in `submission.csv`

## 📚 Libraries Used

- pandas
- numpy
- matplotlib / seaborn (for EDA)
- scikit-learn

## 🧠 ML Concept

This is a **regression problem** because the target variable (`SalePrice`) is continuous numerical data.

## 🧾 License

This project is for learning and demonstration purposes only.


