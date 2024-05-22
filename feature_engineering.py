import pandas as pd

# Load data from CSV file
df = pd.read_csv('data.csv')

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned data to a new CSV file
df.to_csv('cleaned_data.csv', index=False)

# Print the top 5 rows of the cleaned dataframe
print(df.head(5))