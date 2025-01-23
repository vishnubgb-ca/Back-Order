import pandas as pd

# Assuming df is your DataFrame
df = pd.read_csv("data.csv")

# Check if DataFrame is empty
if df.empty:
    print("DataFrame is empty")
else:
    # Extract the first five (head) and last five (tail) rows
    print("First five rows:")
    print(df.head())
    print("\nLast five rows:")
    print(df.tail())

    # Generate a summary of statistical data
    print("\nSummary of statistical data:")
    print(df.describe())

    # Obtain a data frame summary
    print("\nDataFrame summary:")
    print(df.info())

    # Check the data structure
    print("\nData structure:")
    print(df.shape)

    # Determine the column names
    print("\nColumn names:")
    print(df.columns)

    # Check for missing values
    print("\nMissing values:")
    print(df.isnull().sum())

    # Find unique values in each column
    print("\nUnique values in each column:")
    for col in df.columns:
        print(f"{col}: {df[col].unique()}")


