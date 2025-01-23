import pandas as pd
from sklearn.preprocessing import LabelEncoder
from scipy import stats
from imblearn.over_sampling import SMOTE

def remove_outliers(df):
    z_scores = stats.zscore(df)
    abs_z_scores = pd.Series(z_scores).apply(abs)
    filtered_entries = (abs_z_scores < 3)
    return df[filtered_entries]

def remove_feature(df, feature):
    return df.drop(feature, axis=1)

def balance_data(df):
    smote = SMOTE()
    X_smote, y_smote = smote.fit_resample(df.drop("went_on_backorder", axis=1), df["went_on_backorder"])
    return pd.DataFrame(X_smote, columns=df.columns[:-1]), pd.DataFrame(y_smote)

def label_encode(df):
    le = LabelEncoder()
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = le.fit_transform(df[col])
    return df

def transform_data(df):
    df = label_encode(df)
   # df = remove_outliers(df)
    df = remove_feature(df, "sku")
    df, _ = balance_data(df)
 
    return df

# Assuming df is your DataFrame
df = pd.read_csv("data.csv")
df = transform_data(df)
print("Transformed data:", df)
df.to_csv("cleaned_data.csv")

