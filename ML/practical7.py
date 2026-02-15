# Practical 07: Multiple Linear Regression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
cleaned_data = pd.read_csv("housing.csv")

# Multiple Linear Regression implementation
def multiple_linear_regression_manual(X, y):
    """Manually implement multiple linear regression using matrix operations"""
    # Add bias column (intercept term)
    X_with_bias = np.column_stack([np.ones(len(X)), X])
    
    # Calculate coefficients using normal equation: β = (X^T X)^(-1) X^T y
    X_transpose = X_with_bias.T
    XTX = X_transpose @ X_with_bias
    XTy = X_transpose @ y
    coefficients = np.linalg.inv(XTX) @ XTy
    
    # Make predictions
    y_pred = X_with_bias @ coefficients
    
    # Calculate R-squared
    ss_res = np.sum((y - y_pred)**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r_squared = 1 - (ss_res / ss_tot)
    
    # Calculate MSE and RMSE
    mse = np.mean((y - y_pred)**2)
    rmse = np.sqrt(mse)
    
    return coefficients, r_squared, mse, rmse, y_pred

# Apply multiple regression to housing data
def run_multiple_regression(df):
    """Run multiple linear regression on housing data"""
    # Select multiple features for prediction
    features = ['median_income', 'housing_median_age', 'total_rooms', 'total_bedrooms']
    X = df[features].values
    y = df['median_house_value'].values
    
    # Perform multiple regression
    coefficients, r2, mse, rmse, predictions = multiple_linear_regression_manual(X, y)
    
    # Print results
    print(f"📊 Multiple Linear Regression Results:")
    print(f"Intercept: {coefficients[0]:.2f}")
    for i, feature in enumerate(features):
        print(f"{feature}: {coefficients[i+1]:.2f}")
    print(f"R-squared: {r2:.4f}")
    print(f"MSE: {mse:.2f}")
    print(f"RMSE: {rmse:.2f}")
    
    # Plot actual vs predicted
    plt.figure(figsize=(10, 6))
    plt.scatter(y, predictions, alpha=0.6)
    plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', linewidth=2)
    plt.xlabel('Actual House Value ($)')
    plt.ylabel('Predicted House Value ($)')
    plt.title(f'Multiple Linear Regression (R² = {r2:.3f})')
    plt.grid(True)
    plt.show()
    
    print("✅ Multiple Linear Regression completed")
    return coefficients, r2, mse, rmse

# Run multiple regression
mlr_coefficients, mlr_r2, mlr_mse, mlr_rmse = run_multiple_regression(cleaned_data)