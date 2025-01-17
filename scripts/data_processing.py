import pandas as pd
import os

def preprocess_data():
    # Define file paths
    raw_file_path = 'data/raw/Titanic-Dataset.csv'
    cleaned_file_path = 'data/cleaned_data/cleaned_data.csv'

    # Check if the output directory exists, if not, create it
    if not os.path.exists('data/cleaned_data'):
        os.makedirs('data/cleaned_data')

    # Load raw data
    print(f"Loading the file: {raw_file_path}")
    data = pd.read_csv(raw_file_path)

    # Show the first few rows and column names
    print(f"First rows of the raw data:\n{data.head()}")
    print(f"Column names in the raw data:\n{data.columns}")

    # Example preprocessing step: drop rows with missing 'Age' values
    data = data.dropna(subset=['Age'])
    
    # Example of filling missing values for 'Embarked' with the most frequent value
    data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])

    # Save cleaned data
    print(f"Saving the cleaned data to: {cleaned_file_path}")
    data.to_csv(cleaned_file_path, index=False)

# Run preprocessing
preprocess_data()