Titanic - Exploratory Data Analysis

🚀 Project Overview

This project is a comprehensive Exploratory Data Analysis (EDA) on the well-known Titanic dataset, designed to uncover insights about passenger survival rates based on various demographic and socio-economic features. With a clear focus on professionalism, problem-solving, and practical application, the project aims to explore patterns and relationships that influenced survival outcomes — insights crucial for building accurate predictive models.

In the latest version, the project has been enhanced with interactive visualizations, advanced data exploration techniques, and a robust logging system to ensure transparency, traceability, and maintainability of the analysis pipeline.

🎯 Project Goals
	•	Data Cleaning & Preprocessing: Handle missing values, format data, and prepare it for analysis.
	•	Statistical Analysis: Summarize key numerical and categorical features.
	•	Exploratory Data Analysis (EDA): Identify patterns, trends, and relationships influencing survival rates.
	•	Advanced Visualizations:
	•	Static Visualizations: Histograms, box plots, and correlation heatmaps.
	•	Interactive Visualizations: Dynamic charts for deeper insights and user engagement.
	•	Logging System Implementation: Ensure detailed tracking of each processing step for full transparency.
	•	Actionable Insights: Draw meaningful conclusions that could enhance predictive model performance.

🛠️ Tools & Libraries Used
	•	Programming Language: 🐍 Python — Ideal for data analysis and machine learning projects.
	•	Data Manipulation: pandas — For efficient data cleaning and transformation.
	•	Numerical Operations: numpy — For array operations and mathematical functions.
	•	Statistical Analysis: seaborn — For creating informative statistical visualizations.
	•	Data Visualization:
	•	matplotlib — For static visualizations like histograms and heatmaps.
	•	plotly — For interactive, drill-down charts that enhance user experience.
	•	Logging: logging — Tracks key processing steps, aiding in debugging and transparency.
	•	Containerization: Docker — Ensures a consistent development and deployment environment.

🗂 Dataset Description

The Titanic dataset contains information on passengers aboard the Titanic, including:

Feature	Description
PassengerId	Unique ID for each passenger
Survived	Survival status (0 = No, 1 = Yes)
Pclass	Ticket class (1st, 2nd, 3rd)
Name	Passenger’s full name
Sex	Gender
Age	Age of the passenger
SibSp	# of siblings/spouses aboard
Parch	# of parents/children aboard
Ticket	Ticket number
Fare	Ticket fare
Cabin	Cabin number
Embarked	Port of embarkation

📈 Steps Taken in the Project

1️⃣ Data Loading:
	•	Load and inspect the raw dataset from data/raw/.

2️⃣ Data Cleaning & Preprocessing:
	•	Handle missing values (Age, Cabin, Embarked).
	•	Transform categorical data for consistency and usability.
	•	Save the cleaned dataset in data/cleaned_data/cleaned_data.csv.

3️⃣ Exploratory Data Analysis (EDA):
	•	Generate descriptive statistics.
	•	Analyze survival rates across different passenger classes, genders, and age groups.
	•	Perform correlation analysis to assess feature relationships.

4️⃣ Advanced Data Visualization:
	•	Static Visualizations: Boxplots, heatmaps, and survival rate charts.
	•	Interactive Visualizations:
	•	interactive_distribution_of_age.html — Age distribution analysis.
	•	interactive_survival_rate_by_pclass.html — Survival rate by class.
	•	interactive_survival_rate_by_sex.html — Survival rate by gender.

5️⃣ Logging Implementation:
	•	Logs every critical step (data loading, cleaning, analysis, and visualization).
	•	Logs stored in logs/ for traceability and debugging.

6️⃣ Containerization (Optional):
	•	Dockerfile provided for seamless deployment and consistent environments.

🏗 Folder Structure

Titanic-Exploratory-Data-Analysis/
│
├── data/                          # Dataset folder
│   ├── raw/                       # Raw dataset
│   ├── cleaned_data/              # Cleaned and preprocessed data
│
├── results/                       # Analysis and visual results
│   ├── charts/                    # Static and interactive visualizations
│   ├── summary_statistics.txt     # Key data insights and analysis results
│
├── scripts/                       # Python scripts for modular functionality
│   ├── data_processing.py         # Data cleaning and preparation
│   ├── analysis.py                # Exploratory data analysis
│   ├── visualization.py           # Static and interactive visualizations
│
├── logs/                          # Logs for debugging and process tracking
│
├── Dockerfile                     # Containerization configuration
├── requirements.txt               # Python dependencies
├── main.py                        # Main entry point for the project
└── README.md                      # Project documentation

▶️ How to Run the Project

1️⃣ Clone the Repository:

git clone https://github.com/erenaktuerk/Titanic-Exploratory-Data-Analysis.git

2️⃣ Navigate to the Project Directory:

cd Titanic-Exploratory-Data-Analysis

3️⃣ Install Dependencies:

pip install -r requirements.txt

4️⃣ Run the Main Script:

python main.py

5️⃣ (Optional) Run with Docker:

docker build -t titanic-eda .
docker run -p 8050:8050 titanic-eda

🌐 Interactive Visualizations

Once the project runs successfully, you can explore interactive charts stored in the results/charts/ folder by opening .html files directly in your browser.

📝 Future Improvements
	•	Advanced Feature Engineering for more robust survival predictions.
	•	Machine Learning Model Integration to predict survival based on explored insights.
	•	Deployment of an Interactive Dashboard using frameworks like Dash or Streamlit.

💡 Key Takeaways
	•	Enhanced Analytical Depth: Through advanced visualizations and exploratory techniques.
	•	Improved Transparency: By implementing a well-structured logging system.
	•	Real-World Relevance: Gained actionable insights that can inform future survival prediction models.

Let’s take Titanic EDA to the next level! 🚢💡