# Practical 03: Data cleaning and preprocessing
import pandas as pd
import numpy as np


# Data cleaning and preprocessing function
def clean_housing_data(df):
    """Clean and preprocess the housing dataset"""
    df_clean = df.copy()
    
    # Handle missing values in total_bedrooms
    missing_bedrooms = df_clean['total_bedrooms'].isnull().sum()
    print(f"Missing values in total_bedrooms: {missing_bedrooms}")
    
    # Fill missing values with median
    median_bedrooms = df_clean['total_bedrooms'].median()
    df_clean['total_bedrooms'].fillna(median_bedrooms, inplace=True)
    
    # Create new meaningful features
    df_clean['rooms_per_household'] = df_clean['total_rooms'] / df_clean['households']
    df_clean['bedrooms_per_room'] = df_clean['total_bedrooms'] / df_clean['total_rooms']
    df_clean['population_per_household'] = df_clean['population'] / df_clean['households']
    
    # Remove outliers using IQR method for target variable
    Q1 = df_clean['median_house_value'].quantile(0.25)
    Q3 = df_clean['median_house_value'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Filter outliers
    df_clean = df_clean[(df_clean['median_house_value'] >= lower_bound) & 
                       (df_clean['median_house_value'] <= upper_bound)]
    
    print(f"✅ Data cleaned. New shape: {df_clean.shape}")
    return df_clean

# Clean the data
cleaned_data = clean_housing_data(housing_data)