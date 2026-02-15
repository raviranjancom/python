# Practical 01: Loading California Housing dataset from GitHub
# Import essential Python libraries for data manipulation, HTTP requests, and visualization
import pandas as pd
import numpy as np
import requests
from io import StringIO
import matplotlib.pyplot as plt

# Define GitHub raw URL for California Housing dataset
GITHUB_DATA_URL = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

# Function to load data from GitHub
def load_housing_data():
    """Load California Housing dataset from GitHub"""
    try:
        # Fetch data from GitHub
        response = requests.get(GITHUB_DATA_URL)
        # Check if request was successful (status code 200)
        response.raise_for_status()
        # Read CSV data from response text using StringIO
        df = pd.read_csv(StringIO(response.text))
        print(f"✅ Successfully loaded dataset with shape: {df.shape}")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

# Load the dataset
housing_data = load_housing_data()

# Display basic information about the dataset
print(f"Dataset shape: {housing_data.shape}")
print(f"Columns: {list(housing_data.columns)}")
print(f"First 5 rows:")
print(housing_data.head())
