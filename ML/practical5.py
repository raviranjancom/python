# Practical 05: Locally Weighted Regression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Locally Weighted Regression implementation
def locally_weighted_regression(X, y, query_point, tau=0.3):
    """Implement Locally Weighted Regression using Gaussian kernel"""
    # Convert to numpy arrays
    X = np.array(X)
    y = np.array(y)
    
    # Calculate distances from query point
    distances = np.sqrt(np.sum((X - query_point)**2, axis=1))
    
    # Calculate weights using Gaussian kernel
    weights = np.exp(-(distances**2) / (2 * tau**2))
    
    # Add bias term to feature matrix
    X_with_bias = np.column_stack([np.ones(len(X)), X])
    
    # Create diagonal weight matrix
    W = np.diag(weights)
    
    # Calculate weights using normal equation: (X^T W X)^(-1) X^T W y
    theta = np.linalg.inv(X_with_bias.T @ W @ X_with_bias) @ X_with_bias.T @ W @ y
    
    # Make prediction
    query_with_bias = np.array([1, query_point])
    prediction = query_with_bias @ theta
    
    return prediction, theta, weights

# Test LWR with housing data
def test_lwr_on_housing(df):
    """Test LWR on housing dataset using median_income to predict house_value"""
    X = df['median_income'].values[:100]  # Use subset for visualization
    y = df['median_house_value'].values[:100]
    
    # Create query points for smooth curve
    query_points = np.linspace(X.min(), X.max(), 50)
    predictions = []
    
    # Make predictions for each query point
    for qp in query_points:
        pred, theta, weights = locally_weighted_regression(X, y, qp, tau=0.5)
        predictions.append(pred)
    
    # Plot results
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, alpha=0.6, label='Actual Data')
    plt.plot(query_points, predictions, 'r-', linewidth=2, label='LWR Prediction')
    plt.xlabel('Median Income')
    plt.ylabel('Median House Value ($)')
    plt.title('Locally Weighted Regression on Housing Data')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print("✅ Locally Weighted Regression completed")
    return predictions

# Run LWR test
lwr_predictions = test_lwr_on_housing(cleaned_data)