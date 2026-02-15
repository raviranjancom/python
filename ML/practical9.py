# Practical 09: FIND-S Algorithm
import pandas as pd
import numpy as np

import pandas as pd
cleaned_data = pd.read_csv("housing.csv")

# FIND-S Algorithm Implementation
def create_house_categories(df):
    """Create categorical target for house price ranges"""
    df_cat = df.copy()
    
    # Create price categories based on quantiles
    q1 = df['median_house_value'].quantile(0.33)
    q2 = df['median_house_value'].quantile(0.67)
    
    df_cat['price_category'] = pd.cut(df['median_house_value'],
                                bins=[0, q1, q2, float('inf')],
                                labels=['Low', 'Medium', 'High'])
    
    # Discretize features for FIND-S algorithm
    df_cat['income_level'] = pd.cut(df['median_income'], bins=3, labels=['Low', 'Medium', 'High'])
    df_cat['age_level'] = pd.cut(df['housing_median_age'], bins=3, labels=['New', 'Medium', 'Old'])
    df_cat['room_level'] = pd.cut(df['total_rooms'], bins=3, labels=['Small', 'Medium', 'Large'])
    
    return df_cat

# FIND-S Algorithm
def find_s_algorithm(df, target_col='price_category'):
    """Implement FIND-S algorithm for concept learning"""
    # Prepare training data
    features = ['income_level', 'age_level', 'room_level']
    X = df[features].values
    y = df[target_col].values
    
    # Initialize most specific hypothesis
    hypothesis = ['Φ'] * len(features)
    
    print(f"🔍 FIND-S Algorithm Execution:")
    print(f"Initial hypothesis: {hypothesis}")
    
    # Process each positive example
    for i, (example, label) in enumerate(zip(X, y)):
        if label == 'High':  # Positive example
            print(f"\nProcessing positive example {i+1}: {example}")
            
            for j, (attr, hyp) in enumerate(zip(example, hypothesis)):
                if hyp == 'Φ':  # First positive example
                    hypothesis[j] = attr
                elif hyp != attr:  # Generalize the hypothesis
                    hypothesis[j] = '?'
            print(f"Updated hypothesis: {hypothesis}")
    
    # Test the learned hypothesis
    correct_predictions = 0
    total_predictions = 0
    
    print(f"\n🧪 Testing learned hypothesis: {hypothesis}")
    for i, (example, true_label) in enumerate(zip(X[:10], y[:10])):  # Test on first 10 examples
        predicted = True
        for attr, hyp in zip(example, hypothesis):
            if hyp != '?' and hyp != attr:
                predicted = False
                break
        
        pred_label = 'High' if predicted else 'Not High'
        correct = (pred_label == true_label)
        correct_predictions += correct
        total_predictions += 1
        print(f"Example {i+1}: {example} -> Predicted: {pred_label}, Actual: {true_label}, {'✓' if correct else '✗'}")
    
    accuracy = correct_predictions / total_predictions
    print(f"\n📊 FIND-S Results:")
    print(f"Final hypothesis: {hypothesis}")
    print(f"Accuracy: {accuracy:.2%} ({correct_predictions}/{total_predictions})")
    
    print("✅ FIND-S Algorithm completed")
    return hypothesis, accuracy

# Run FIND-S algorithm
df_categorical = create_house_categories(cleaned_data)
final_hypothesis, find_s_accuracy = find_s_algorithm(df_categorical)
