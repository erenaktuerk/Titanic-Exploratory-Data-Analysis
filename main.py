import logging
import pandas as pd
from scripts.data_processing import preprocess_data
from scripts.analysis import perform_analysis
from scripts.visualization import create_visualizations, create_boxplots, create_interactive_visualizations

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting data preprocessing...")
    preprocess_data()  # Calls data processing script

    # Load the cleaned data
    try:
        cleaned_data = pd.read_csv('data/cleaned_data/cleaned_data.csv')
        logger.info("Cleaned data loaded successfully.")
    except Exception as e:
        logger.error("Error loading cleaned data: %s", e)
        return

    logger.info("Starting exploratory data analysis...")
    perform_analysis(cleaned_data)

    logger.info("Starting data visualizations...")
    create_visualizations(cleaned_data)
    create_boxplots(cleaned_data)
    create_interactive_visualizations(cleaned_data)

if __name__ == "__main__":
    main()