
import os
import boto3
import pandas as pd
from io import StringIO

# Get AWS credentials from environment variables
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key = os.getenv("aws_secret_access_key")
bucket = os.getenv("bucket")
region = os.getenv("region")
key = os.getenv("key")

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region
)

# Create an S3 resource object using the session
s3 = session.resource("s3")

# Get the bucket object
bucket_obj = s3.Bucket(bucket)

# Get the object from the bucket
obj = bucket_obj.Object(key=key)

# Read the object content
response = obj.get()
data = response["Body"].read().decode("utf-8")

# Convert the data to a pandas DataFrame
df = pd.read_csv(StringIO(data))

# Save the DataFrame to a CSV file
df.to_csv("data.csv", index=False)

# Display the top 5 rows of the DataFrame
print(df.head())

