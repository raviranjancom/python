# Practical 06: Simple Linear Regression
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

import pandas as pd
cleaned_data = pd.read_csv("housing.csv")

# Simple Linear Regression implementation
def simple_linear_regression_manual(X, y):
    """Manually implement simple linear regression using least squares"""
    n = len(X)
    
    # Calculate means
    mean_x = np.mean(X)
    mean_y = np.mean(y)
    
    # Calculate slope (beta_1) using least squares formula
    numerator = np.sum((X - mean_x) * (y - mean_y))
    denominator = np.sum((X - mean_x)**2)
    slope = numerator / denominator
    
    # Calculate intercept (beta_0)
    intercept = mean_y - slope * mean_x
    
    # Make predictions
    y_pred = slope * X + intercept
    
    # Calculate R-squared
    ss_res = np.sum((y - y_pred)**2)
    ss_tot = np.sum((y - mean_y)**2)
    r_squared = 1 - (ss_res / ss_tot)
    
    # Calculate Mean Squared Error
    mse = np.mean((y - y_pred)**2)
    
    return slope, intercept, r_squared, mse, y_pred

# Apply to housing data
def run_simple_regression(df):
    """Run simple linear regression on housing data"""
    # Prepare data
    X = df['median_income'].values
    y = df['median_house_value'].values
    
    # Perform regression
    slope, intercept, r2, mse, predictions = simple_linear_regression_manual(X, y)
    
    # Print results
    print(f"📊 Simple Linear Regression Results:")
    print(f"Slope (β₁): {slope:.2f}")
    print(f"Intercept (β₀): {intercept:.2f}")
    print(f"R-squared: {r2:.4f}")
    print(f"Mean Squared Error: {mse:.2f}")
    
    # Plot results
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, alpha=0.6, label='Actual Data')
    plt.plot(X, predictions, 'r-', linewidth=2, label=f'Regression Line (R² = {r2:.3f})')
    plt.xlabel('Median Income')
    plt.ylabel('Median House Value ($)')
    plt.title('Simple Linear Regression: Income vs House Value')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print("✅ Simple Linear Regression completed")
    return slope, intercept, r2, mse

# Run the regression
slope, intercept, r2, mse = run_simple_regression(cleaned_data)