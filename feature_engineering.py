import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from scipy import stats
import numpy as np

# Load data
df = pd.read_csv('data.csv')

# Row Deletion
#df = df[df['national_inv'] != 'True']

# Duplicate values
df.drop_duplicates(inplace=True)

# Label encoding
le = LabelEncoder()
df['potential_issue'] = le.fit_transform(df['potential_issue'])
df['oe_constraint'] = le.fit_transform(df['oe_constraint'])
df['ppap_risk'] = le.fit_transform(df['ppap_risk'])
df['stop_auto_buy'] = le.fit_transform(df['stop_auto_buy'])
df['went_on_backorder'] = le.fit_transform(df['went_on_backorder'])
print(df.head())



# One-hot encoding
ohe = OneHotEncoder()
df = pd.concat([df, pd.DataFrame(ohe.fit_transform(df[['rev_stop']]).toarray(), columns=ohe.get_feature_names_out(['rev_stop']))], axis=1)
print("Data types after encoding:\n", df.dtypes)

# Feature deletion
df = df.drop(['sku', 'lead_time'], axis=1)

# Outliers
for column in [{'label': 'national_inv', 'value': 'national_inv'}, {'label': 'in_transit_qty', 'value': 'in_transit_qty'}, {'label': 'forecast_3_month', 'value': 'forecast_3_month'}, {'label': 'forecast_6_month', 'value': 'forecast_6_month'}, {'label': 'forecast_9_month', 'value': 'forecast_9_month'}, {'label': 'sales_1_month', 'value': 'sales_1_month'}, {'label': 'sales_3_month', 'value': 'sales_3_month'}, {'label': 'sales_6_month', 'value': 'sales_6_month'}, {'label': 'sales_9_month', 'value': 'sales_9_month'}, {'label': 'min_bank', 'value': 'min_bank'}, {'label': 'pieces_past_due', 'value': 'pieces_past_due'}, {'label': 'local_bo_qty', 'value': 'local_bo_qty'}]:
    Q1 = df[column['value']].quantile(0.25)
    Q3 = df[column['value']].quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df[column['value']] < (Q1 - 1.5 * IQR)) |(df[column['value']] > (Q3 + 1.5 * IQR)))]

# Save cleaned data
df.to_csv('cleaned_data.csv', index=False)

# Print top 5 rows
print(df.head())