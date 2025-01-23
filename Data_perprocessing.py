import pandas as pd
df = pd.read_csv("data.csv")
# Assuming df is your DataFrame
df = df.dropna()  # remove missing values
df = df.drop_duplicates()  # remove duplicate rows
df.to_csv("data.csv")
print(df)

