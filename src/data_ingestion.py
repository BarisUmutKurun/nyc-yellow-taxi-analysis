import pandas as pd
import logging
from functools import reduce


def load_data(months, base_url="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"):
    logging.info("Loading data for months: %s", months)
    data_frames = []

    for month in months:
        url = f"{base_url}{month}.parquet"
        logging.info("Loading data from %s", url)
        df = pd.read_parquet(url)
        data_frames.append(df)
    
    # Concatenate all dataframes in chunks to reduce memory usage
    data = reduce(lambda left, right: pd.concat([left, right], ignore_index=True), data_frames)
        # Calculate memory usage in bytes
    memory_bytes = data.memory_usage(deep=True).sum()

    # Convert bytes to megabytes
    memory_mb = memory_bytes / (1024 ** 2)
    length = len(data)
    logging.info(f"Memory usage: {memory_mb}")
    logging.info(f"Data len: {length}")
    logging.info("Data loading completed")
    return data

def clean_data(data):
    logging.info("Cleaning data")
    data = data.dropna(subset=['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'trip_distance'])
    data['tpep_pickup_datetime'] = pd.to_datetime(data['tpep_pickup_datetime'], errors='coerce')
    data['tpep_dropoff_datetime'] = pd.to_datetime(data['tpep_dropoff_datetime'], errors='coerce')
    data = data.dropna(subset=['tpep_pickup_datetime', 'tpep_dropoff_datetime'])
    data = data[(data['tpep_pickup_datetime'] >= '2024-01-01') & (data['tpep_pickup_datetime'] <= '2024-03-31')]
    data['trip_duration'] = (data['tpep_dropoff_datetime'] - data['tpep_pickup_datetime']).dt.total_seconds() / 60
    data = data[(data['trip_duration'] > 0) & (data['trip_duration'] < 1440)]
    data = data[(data['trip_distance'] > 0) & (data['trip_distance'] < 100)]
    logging.info("Data cleaning completed")
    return data

def save_cleaned_data(data, file_path):
    logging.info("Saving cleaned data to %s", file_path)
    data.to_parquet(file_path)
    logging.info("Cleaned data saved")
