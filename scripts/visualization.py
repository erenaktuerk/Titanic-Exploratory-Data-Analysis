import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
import os
charts_dir = 'results/charts'

def create_visualizations(data):
    # Set the style of the plots
    sns.set(style="whitegrid")
    
    # Create the charts directory if it doesn't exist
    if not os.path.exists(charts_dir):
        os.makedirs(charts_dir)

    # Plot 1: Distribution of Age
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Age'], kde=True, color='blue', bins=30)
    plt.title('Distribution of Age')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.savefig(f'{charts_dir}/distribution_of_age.png')  # Save plot as PNG
    plt.close()  # Close the plot to avoid overlapping with the next

    # Plot 2: Survival Rate by Sex
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Sex', y='Survived', data=data)
    plt.title('Survival Rate by Sex')
    plt.xlabel('Sex')
    plt.ylabel('Survival Rate')
    plt.savefig(f'{charts_dir}/survival_rate_by_sex.png')
    plt.close()

    # Plot 3: Survival Rate by Pclass
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Pclass', y='Survived', data=data)
    plt.title('Survival Rate by Pclass')
    plt.xlabel('Pclass')
    plt.ylabel('Survival Rate')
    plt.savefig(f'{charts_dir}/survival_rate_by_pclass.png')
    plt.close()

    # Plot 4: Correlation Heatmap
    plt.figure(figsize=(10, 8))
    correlation_matrix = data.select_dtypes(include='number').corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix Heatmap')
    plt.savefig(f'{charts_dir}/correlation_matrix_heatmap.png')
    plt.close()

    # Plot 5: Count of Passengers by Pclass
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Pclass', data=data, palette='Set2')
    plt.title('Count of Passengers by Pclass')
    plt.xlabel('Pclass')
    plt.ylabel('Count')
    plt.savefig(f'{charts_dir}/count_of_passengers_by_pclass.png')
    plt.close()

    # Plot 6: Count of Missing Values
    plt.figure(figsize=(10, 6))
    missing_values = data.isnull().sum()
    missing_values = missing_values[missing_values > 0]
    sns.barplot(x=missing_values.index, y=missing_values.values, palette="Blues_d")
    plt.title('Count of Missing Values')
    plt.xlabel('Columns')
    plt.ylabel('Missing Values Count')
    plt.savefig(f'{charts_dir}/count_of_missing_values.png')
    plt.close()
    
def create_boxplots(data):
    # Set the style of the plots
    sns.set(style="whitegrid")
    
    # Boxplot 1: Distribution of Age
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=data['Age'], color='skyblue')
    plt.title('Boxplot of Age')
    plt.xlabel('Age')
    plt.savefig(f'{charts_dir}/boxplot_age.png')
    plt.close()

    # Boxplot 2: Distribution of Fare
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=data['Fare'], color='lightgreen')
    plt.title('Boxplot of Fare')
    plt.xlabel('Fare')
    plt.savefig(f'{charts_dir}/boxplot_fare.png')
    plt.close()

    # Boxplot 3: Distribution of Age by Pclass
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Pclass', y='Age', data=data, palette='Set2')
    plt.title('Boxplot of Age by Pclass')
    plt.xlabel('Pclass')
    plt.ylabel('Age')
    plt.savefig(f'{charts_dir}/boxplot_age_by_pclass.png') 
    plt.close()
    
def create_interactive_visualizations(data):
    """
    Creates interactive visualizations using Plotly and saves them as HTML files.
    """
    # Ensure the charts directory exists
    charts_dir = 'results/charts'
    if not os.path.exists(charts_dir):
        os.makedirs(charts_dir)

    # Interactive Distribution of Age (Histogram with Box marginal)
    fig_age = px.histogram(data, x="Age", nbins=30, title="Interactive Distribution of Age", marginal="box")
    fig_age.write_html(f'{charts_dir}/interactive_distribution_of_age.html')
    fig_age.show()

    # Interactive Survival Rate by Sex
    # First, calculate the mean survival rate by Sex
    survival_by_sex = data.groupby("Sex", as_index=False)["Survived"].mean()
    fig_sex = px.bar(survival_by_sex, x="Sex", y="Survived", title="Interactive Survival Rate by Sex")
    fig_sex.write_html(f'{charts_dir}/interactive_survival_rate_by_sex.html')
    fig_sex.show()

    # Interactive Survival Rate by Pclass
    survival_by_pclass = data.groupby("Pclass", as_index=False)["Survived"].mean()
    fig_pclass = px.bar(survival_by_pclass, x="Pclass", y="Survived", title="Interactive Survival Rate by Pclass")
    fig_pclass.write_html(f'{charts_dir}/interactive_survival_rate_by_pclass.html')
    fig_pclass.show()