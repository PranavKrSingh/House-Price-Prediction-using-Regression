import sys
from pathlib import Path
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

BASE_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = BASE_DIR / 'src'
sys.path.insert(0, str(SRC_DIR))

from data_preprocessing import load_data, preprocess_data
from feature_engineering import add_features

def train_and_evaluate():
    print("📦 Starting pipeline...")
    train_path = BASE_DIR / 'data' / 'raw' / 'train.csv'
    test_path  = BASE_DIR / 'data' / 'raw' / 'test.csv'

    train_df, test_df = load_data(train_path, test_path)
    print(f"✅ Train shape: {train_df.shape}, Test shape: {test_df.shape}")

    train_df = preprocess_data(train_df)
    test_df  = preprocess_data(test_df)

    train_df = add_features(train_df)
    test_df  = add_features(test_df)

    X = train_df.drop(['Id', 'SalePrice'], axis=1, errors='ignore')
    y = train_df['SalePrice']

    X = pd.get_dummies(X)
    test_X = pd.get_dummies(test_df.drop(['Id'], axis=1, errors='ignore'))
    test_X = test_X.reindex(columns=X.columns, fill_value=0)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    scores = cross_val_score(model, X, y, cv=5, scoring='neg_root_mean_squared_error')
    mean_rmse = -scores.mean()
    print(f'📊 5-Fold CV RMSE: {mean_rmse:.2f}')

    model.fit(X, y)
    preds = model.predict(test_X)

    submission = pd.DataFrame({'Id': test_df['Id'], 'SalePrice': preds})
    out_path = BASE_DIR / 'submission.csv'
    submission.to_csv(out_path, index=False)
    print(f"✅ Submission saved to {out_path}")

if __name__ == '__main__':
    train_and_evaluate()
