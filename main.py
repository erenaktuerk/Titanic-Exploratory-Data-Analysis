import pandas as pd
from scripts.data_processing import preprocess_data
from scripts.analysis import perform_analysis
from scripts.visualization import create_visualizations, create_boxplots

def main():
    # Step 1: Data Preprocessing
    print("Starting data preprocessing...")
    preprocess_data()  # Calls data processing script
    
    # Step 2: Load the cleaned data
    cleaned_data = pd.read_csv('data/cleaned_data/cleaned_data.csv')
    
    # Step 3: Exploratory Data Analysis
    print("Starting exploratory data analysis...")
    perform_analysis(cleaned_data)
    
    # Step 4: Data Visualization
    print("Starting data visualizations...")
    create_visualizations(cleaned_data)
    create_boxplots(cleaned_data)

if __name__ == "__main__":
    main()