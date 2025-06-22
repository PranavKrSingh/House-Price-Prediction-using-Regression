def add_features(df):
    df = df.copy()
    df['TotalBath'] = (
        df.get('BsmtFullBath', 0) +
        0.5 * df.get('BsmtHalfBath', 0) +
        df.get('FullBath', 0) +
        0.5 * df.get('HalfBath', 0)
    )
    df['TotalSF'] = (
        df.get('TotalBsmtSF', 0) +
        df.get('1stFlrSF', 0) +
        df.get('2ndFlrSF', 0)
    )
    return df
