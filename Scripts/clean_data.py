# clean_data.py
# This script cleans raw data and outputs a processed dataset.

import pandas as pd

# Load raw data
raw_data = pd.read_csv('../Data/raw_data.csv')  # Adjust path if needed

# Cleaning step: Drop rows with missing values
cleaned_data = raw_data.dropna()

# Save cleaned data
cleaned_data.to_csv('../Data/cleaned_data.csv', index=False)

print("Data cleaning completed successfully!")
