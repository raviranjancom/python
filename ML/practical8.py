# Practical 08: Advanced Regression - Random Forest
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# Load cleaned housing data
cleaned_data = pd.read_csv("housing.csv")

# Random Forest implementation
def random_forest_regression(df, n_estimators=100):
    """Implement Random Forest regression for house price prediction"""
    
    # Prepare features and target
    features = [
        'median_income',
        'housing_median_age',
        'total_rooms',
        'total_bedrooms',
        'population',
        'households',
        'latitude',
        'longitude'
    ]
    
    X = df[features].values
    y = df['median_house_value'].values
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Create and train Random Forest model
    rf_model = RandomForestRegressor(
        n_estimators=n_estimators,
        random_state=42
    )
    rf_model.fit(X_train, y_train)
    
    # Make predictions
    y_train_pred = rf_model.predict(X_train)
    y_test_pred = rf_model.predict(X_test)
    
    # Calculate metrics
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)
    train_mae = mean_absolute_error(y_train, y_train_pred)
    test_mae = mean_absolute_error(y_test, y_test_pred)
    
    # Print results
    print("🌲 Random Forest Regression Results:")
    print(f"Training R²: {train_r2:.4f}")
    print(f"Testing R²:  {test_r2:.4f}")
    print(f"Training MAE: {train_mae:.2f}")
    print(f"Testing MAE:  {test_mae:.2f}")
    
    # Feature importance
    feature_importance = rf_model.feature_importances_
    importance_df = pd.DataFrame({
        'feature': features,
        'importance': feature_importance
    }).sort_values('importance', ascending=False)
    
    print("\nFeature Importance:")
    print(importance_df)
    
    # Plot predictions vs actual and feature importance
    plt.figure(figsize=(12, 5))
    
    # Subplot 1: Actual vs Predicted
    plt.subplot(1, 2, 1)
    plt.scatter(y_test, y_test_pred, alpha=0.6)
    plt.plot(
        [y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        'r--',
        linewidth=2
    )
    plt.xlabel('Actual House Value')
    plt.ylabel('Predicted House Value')
    plt.title(f'Random Forest (R² = {test_r2:.3f})')
    plt.grid(True)
    
    # Subplot 2: Feature Importance
    plt.subplot(1, 2, 2)
    plt.barh(importance_df['feature'], importance_df['importance'])
    plt.xlabel('Importance')
    plt.title('Feature Importance')
    plt.gca().invert_yaxis()
    
    plt.tight_layout()
    plt.show()
    
    print("✅ Random Forest Regression completed")
    return rf_model, test_r2, test_mae, importance_df

# Run Random Forest regression
rf_model, rf_r2, rf_mae, importance_df = random_forest_regression(cleaned_data)
