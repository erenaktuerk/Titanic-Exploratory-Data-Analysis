

import pandas as pd

def perform_analysis(data):
    # Basic descriptive statistics
    print("\nBasic Descriptive Statistics:")
    print(data.describe())
    
    # Correlation matrix to analyze relationships between numeric features
    print("\nCorrelation Matrix:")
    print(data.corr())
    
    # Count of unique values in categorical columns
    print("\nCount of Unique Values in Categorical Columns:")
    print(data.select_dtypes(include=['object']).nunique())
    
    # Count of missing values in each column
    print("\nMissing Values in Each Column:")
    print(data.isnull().sum())
    
    # Survival rate based on Sex
    print("\nSurvival rate based on Sex:")
    print(data.groupby('Sex')['Survived'].mean())
    
    # Survival rate based on Pclass
    print("\nSurvival rate based on Pclass:")
    print(data.groupby('Pclass')['Survived'].mean())
    
    # Average age of passengers
    print("\nAverage age of passengers:")
    print(data['Age'].mean())
    
    # Count of passengers by class
    print("\nCount of passengers by class:")
    print(data['Pclass'].value_counts())
    
    # Survival rate by class and sex
    print("\nSurvival rate by class and sex:")
    print(data.groupby(['Pclass', 'Sex'])['Survived'].mean())