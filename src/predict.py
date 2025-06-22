import sys
from pathlib import Path
import pandas as pd
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = BASE_DIR / 'src'
sys.path.insert(0, str(SRC_DIR))

from data_preprocessing import preprocess_data
from feature_engineering import add_features

def predict_new_data(input_path, model_path):
    df = pd.read_csv(input_path)
    df = preprocess_data(df)
    df = add_features(df)
    df = pd.get_dummies(df)

    model = joblib.load(model_path)
    preds = model.predict(df)
    return preds
