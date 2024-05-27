# NYC Yellow Taxi Analysis

## Overview

This project focuses on analyzing the NYC Yellow Taxi data to uncover insights and trends related to taxi rides in New York City. The analysis includes data preprocessing, exploratory data analysis (EDA), and visualization of key metrics.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Details](#project-details)
- [Contact](#contact)

## Installation

To set up this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/BarisUmutKurun/nyc-yellow-taxi-analysis.git
   cd nyc-yellow-taxi-analysis
2. Set up a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   poetry install
3. Set up Docker (optional):
   ```bash
   docker-compose up

## Usage

To run the analysis, execute the following commands:

1. Navigate to the src directory:
   ```bash
   cd src
2. Run the analysis script:
   ```bash
   python main.py

The results will be saved in the results directory.

## Project Details

### Task Context

1. Data Source: NYC Yellow Taxi data from [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).
2. Task Requirements:

   - Calculate the average trip length of all Yellow Taxis for a month.

   - Extend this to a data pipeline that can ingest new data and calculate the 45-day rolling average trip length.

   - Ensure the program is suitable for a production setup.

   - Document how the pipeline would scale to handle data sizes that exceed a single machine's capacity.

### Scaling the Pipeline

To scale the pipeline to handle larger datasets that do not fit on a single machine, the following approaches can be considered:

   - Distributed Computing: Utilize frameworks like Apache Spark or Dask to distribute the processing across multiple nodes.

   - Cloud Services: Leverage cloud-based services such as AWS EMR, Google Cloud Dataproc, or Azure HDInsight to handle large-scale data processing.

   - Data Partitioning: Split the data into smaller, manageable chunks and process them in parallel.

   - Optimized Storage: Use efficient data storage formats like Parquet or ORC, which support columnar storage and efficient compression.
   

## Contact

For any questions or issues, please contact BarisUmutKurun at bumutkurun@gmail.com



