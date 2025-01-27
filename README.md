Data Pipeline Project



Overview

This project involves the creation of a data pipeline that collects data from an API, processes and filters the data, and then loads it into a PostgreSQL database. The dataset is further divided into three segments for analysts to work on using views in the database.

Features


Data Collection: Fetches data from a specified API.

Data Processing: Filters and processes the data to extract only the necessary information.

Data Loading: Loads the processed data into a PostgreSQL database.

Data Segmentation: Splits the dataset into three segments for different analysts to work on using views.

Technologies Used


API Source: [https://api.currencyfreaks.com]

Programming Language: Python

Libraries: requests, pandas, SQLAlchemy, psycopg2

Database: PostgreSQL

Views: Created views to segment the data for analysts.

Project Structure


Data Collection: Python script to fetch data from the API.

Data Processing: Filtering and processing the data using Pandas.

Data Loading: Using SQLAlchemy and psycopg2 to load data into PostgreSQL.

Data Segmentation: Creating views in PostgreSQL to divide the dataset into three segments.

Conclusion 


This project demonstrates the effective use of a data pipeline to collect, process, and load data into a PostgreSQL database, with additional segmentation for analytical purposes.
