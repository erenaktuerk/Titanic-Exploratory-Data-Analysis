# Titanic - Exploratory Data Analysis

## Overview
This project performs an exploratory data analysis (EDA) on the Titanic dataset, aiming to uncover insights about passenger survival rates based on various features, including age, sex, and class. The analysis helps understand patterns and correlations that influenced survival.

## Project Goals
- Clean and preprocess the Titanic dataset.
- Perform statistical analysis to summarize key features.
- Visualize important patterns and relationships between variables.
- Generate actionable insights that could help improve survival prediction models.

## Tools and Libraries Used
- *Python*: The primary programming language used for the project.
- *Pandas*: For data manipulation and preprocessing.
- *Matplotlib*: For creating static, animated, and interactive visualizations.
- *Seaborn*: For statistical data visualization.
- *NumPy*: For handling numerical operations and array manipulations.

## Dataset
The dataset used for this project contains the details of passengers aboard the Titanic. It includes features like:
- PassengerId
- Survived (0 = No, 1 = Yes)
- Pclass (Ticket class)
- Name
- Sex
- Age
- SibSp (Siblings and spouses aboard)
- Parch (Parents and children aboard)
- Ticket
- Fare
- Cabin
- Embarked (Port of embarkation)

The dataset is provided in CSV format and is loaded from the data/raw folder.

## Steps Taken in the Project
1. *Data Loading*: Load and inspect the raw dataset.
2. *Data Cleaning*: Handle missing values, preprocess the data for analysis.
3. *Exploratory Data Analysis (EDA)*:
   - Descriptive statistics for numerical and categorical features.
   - Analysis of survival rates based on different variables.
   - Correlation analysis.
4. *Data Visualization*:
   - Histograms, bar plots, box plots, and heatmaps to visualize relationships and distributions.
   - Saving visualizations as PNG files to results/charts.

## Running the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/erenaktuerk/Titanic-Exploratory-Data-Analysis.git

	2.	Navigate to the project folder:

cd Titanic-Exploratory-Data-Analysis


	3.	Install the required dependencies:

pip install -r requirements.txt


	4.	Run the main script to load the dataset, preprocess it, perform EDA, and generate visualizations:

python main.py



Folder Structure

Titanic-Exploratory-Data-Analysis/
│
├── data/                          # Folder for raw and cleaned data
│   ├── raw/                       # Raw input data (Titanic dataset CSV)
│   ├── cleaned_data/              # Cleaned data (cleaned_data.csv)
│
├── scripts/                       # Python scripts for data processing and analysis
│   ├── data_preprocessing.py      # Script for cleaning the data
│   ├── analysis.py                # Script for performing EDA and statistical analysis
│   ├── visualization.py           # Script for generating visualizations
│
├── results/                       # Folder for results and saved visualizations
│   ├── charts/                    # Exported charts (PNG images)
│   └── summary_statistics.txt     # Summary of statistics and analysis
│
├── README.md                      # Project documentation
├── requirements.txt               # List of required Python dependencies
└── main.py                        # Main script to run the entire project

License

This project is licensed under the MIT License - see the LICENSE file for details.
