# Practical 02: Data exploration and analysis
import pandas as pd
import numpy as np


# Function to explore dataset structure
def explore_dataset(df):
    """Perform comprehensive data exploration"""
    print("📊 DATASET OVERVIEW")
    print("=" * 50)
    print(f"Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"\nColumn names: {list(df.columns)}")
    
    # Display data types
    print(f"\nData types:")
    print(df.dtypes)
    
    # Display first few rows
    print(f"\nFirst 5 rows:")
    print(df.head())
    
    # Display statistical summary
    print(f"\nStatistical summary:")
    print(df.describe())
    
    # Check for missing values
    print(f"\nMissing values:")
    print(df.isnull().sum())
    
    return df

# Explore the data
explored_data = explore_dataset(housing_data)