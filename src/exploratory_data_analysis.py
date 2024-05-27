import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Set the matplotlib backend to 'Agg' for headless environments
import matplotlib
matplotlib.use('Agg')

def perform_eda(data):
    
    # Data summary and null value check
    logging.info("Generating data summary")
    summary = data.describe()
    logging.info("Data summary:\n%s", summary)
    
    logging.info("Checking for null values")
    null_values = data.isnull().sum()
    logging.info("Null values:\n%s", null_values)
    
    # Plot distribution of trip duration
    logging.info("Plotting distribution of trip duration")
    plt.figure(figsize=(10, 6))
    sns.histplot(data['trip_duration'], bins=100, kde=True)
    plt.title('Distribution of Trip Duration')
    plt.xlabel('Trip Duration (minutes)')
    plt.ylabel('Frequency')
    plt.savefig('./results/trip_duration_distribution.png')
    plt.close()
    logging.info("Trip duration distribution plot completed")
    
    # Plot distribution of trip distance
    logging.info("Plotting distribution of trip distance")
    plt.figure(figsize=(10, 6))
    sns.histplot(data['trip_distance'], bins=100, kde=True)
    plt.title('Distribution of Trip Distance')
    plt.xlabel('Trip Distance (miles)')
    plt.ylabel('Frequency')
    plt.savefig('./results/trip_distance_distribution.png')
    plt.close()
    logging.info("Trip distance distribution plot completed")
    
    # Plot trip duration vs. trip distance
    logging.info("Plotting trip duration vs. trip distance")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='trip_distance', y='trip_duration', data=data, alpha=0.5)
    plt.title('Trip Duration vs. Trip Distance')
    plt.xlabel('Trip Distance (miles)')
    plt.ylabel('Trip Duration (minutes)')
    plt.savefig('./results/trip_duration_vs_distance.png')
    plt.close()
    logging.info("Trip duration vs. trip distance plot completed")

    logging.info("Exploratory data analysis completed")

if __name__ == "__main__":
    import yaml
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    cleaned_data_file = config['data']['cleaned_data_file']
    
    data = pd.read_parquet(cleaned_data_file)
    perform_eda(data)
