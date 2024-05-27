import pandas as pd
import matplotlib.pyplot as plt
import logging

def calculate_monthly_average(data):
    logging.info("Calculating monthly average trip length")
    data['tpep_pickup_datetime'] = pd.to_datetime(data['tpep_pickup_datetime'])
    data['tpep_dropoff_datetime'] = pd.to_datetime(data['tpep_dropoff_datetime'])
    data['trip_duration'] = (data['tpep_dropoff_datetime'] - data['tpep_pickup_datetime']).dt.total_seconds() / 60
    
    # Filter data to include only the last six months
    data = data[(data['tpep_pickup_datetime'] >= '2024-01-01') & (data['tpep_pickup_datetime'] <= '2024-03-31')]
    
    # Group by month and calculate the mean trip duration
    monthly_avg = data.groupby(data['tpep_pickup_datetime'].dt.to_period('M'))['trip_duration'].mean()
    logging.info("Monthly average calculation completed")
    return monthly_avg

def calculate_rolling_average(data):
    logging.info("Calculating 45-day rolling average trip length")
    data['tpep_pickup_datetime'] = pd.to_datetime(data['tpep_pickup_datetime'])
    data['tpep_dropoff_datetime'] = pd.to_datetime(data['tpep_dropoff_datetime'])
    data['trip_duration'] = (data['tpep_dropoff_datetime'] - data['tpep_pickup_datetime']).dt.total_seconds() / 60

    # Sort by pickup datetime
    data = data.sort_values(by='tpep_pickup_datetime')
    data.set_index('tpep_pickup_datetime', inplace=True)
    
    rolling_avg = data['trip_duration'].rolling(window='45D').mean()
    logging.info("45-day rolling average calculation completed")
    return rolling_avg

def visualize_monthly_average(monthly_avg):
    logging.info("Visualizing monthly average trip length")
    plt.figure(figsize=(10, 6))
    monthly_avg.plot(kind='bar', title="Average Trip Length per Month")
    plt.xlabel("Month")
    plt.ylabel("Average Trip Length (minutes)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('./results/monthly_average_trip_length.png')
    logging.info("Monthly average trip length visualization saved")
    plt.close()

def visualize_rolling_average(rolling_avg):
    logging.info("Visualizing 45-day rolling average trip length")
    plt.figure(figsize=(10, 6))
    rolling_avg.plot(title="45-Day Rolling Average Trip Length")
    plt.xlabel("Date")
    plt.ylabel("Average Trip Length (minutes)")
    plt.tight_layout()
    plt.savefig('./results/rolling_average_trip_length.png')
    logging.info("45-day rolling average trip length visualization saved")
    plt.close()
