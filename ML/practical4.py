# Practical 04: Data visualization
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Function to create comprehensive visualizations
def visualize_housing_data(df):
    """Create comprehensive visualizations of housing data"""
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. Distribution of house values
    axes[0, 0].hist(df['median_house_value'], bins=50, alpha=0.7, color='skyblue')
    axes[0, 0].set_title('Distribution of Median House Value')
    axes[0, 0].set_xlabel('House Value ($)')
    axes[0, 0].set_ylabel('Frequency')
    
    # 2. Scatter plot: Income vs House Value
    axes[0, 1].scatter(df['median_income'], df['median_house_value'], alpha=0.6, color='coral')
    axes[0, 1].set_title('Median Income vs House Value')
    axes[0, 1].set_xlabel('Median Income')
    axes[0, 1].set_ylabel('House Value ($)')
    
    # 3. Geographic distribution
    scatter = axes[1, 0].scatter(df['longitude'], df['latitude'], 
                              c=df['median_house_value'], alpha=0.6, cmap='viridis')
    axes[1, 0].set_title('Geographic Distribution of House Values')
    axes[1, 0].set_xlabel('Longitude')
    axes[1, 0].set_ylabel('Latitude')
    
    # 4. Correlation heatmap
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr()
    im = axes[1, 1].imshow(corr_matrix, cmap='coolwarm', aspect='auto')
    axes[1, 1].set_title('Feature Correlation Heatmap')
    axes[1, 1].set_xticks(range(len(numeric_cols)))
    axes[1, 1].set_yticks(range(len(numeric_cols)))
    axes[1, 1].set_xticklabels(numeric_cols, rotation=45)
    axes[1, 1].set_yticklabels(numeric_cols)
    
    plt.tight_layout()
    plt.show()
    return corr_matrix

# Create visualizations
correlation_matrix = visualize_housing_data(cleaned_data)