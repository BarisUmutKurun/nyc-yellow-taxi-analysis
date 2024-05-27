import logging
import yaml
from data_ingestion import load_data, clean_data, save_cleaned_data
from data_processing import calculate_monthly_average, calculate_rolling_average, visualize_monthly_average, visualize_rolling_average
from exploratory_data_analysis import perform_eda

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        # Load configuration
        with open('./config/config.yaml', 'r') as f:
            config = yaml.safe_load(f)
        months = config['data']['months']
        cleaned_data_file = config['data']['cleaned_data_file']
        
        # Data ingestion and cleaning
        logging.info("Starting data ingestion and cleaning")
        data = load_data(months)
        cleaned_data = clean_data(data)
        save_cleaned_data(cleaned_data, cleaned_data_file)
        logging.info("Data ingestion and cleaning completed")
        
        # Perform EDA
        logging.info("Starting exploratory data analysis")
        perform_eda(cleaned_data)
        logging.info("Exploratory data analysis completed")
        
        # Data processing and visualization
        logging.info("Starting data processing and visualization")
        monthly_avg = calculate_monthly_average(cleaned_data)
        logging.info("Monthly Average Trip Length: %s", monthly_avg)
        visualize_monthly_average(monthly_avg)
        
        rolling_avg = calculate_rolling_average(cleaned_data)
        logging.info("45-Day Rolling Average Trip Length: %s", rolling_avg)
        visualize_rolling_average(rolling_avg)
        logging.info("Data processing and visualization completed")
        
    except Exception as e:
        logging.error("An error occurred: %s", e)
        raise

if __name__ == "__main__":
    main()
