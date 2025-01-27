import requests
import pandas as pd
from sqlalchemy import create_engine

url = 'https://api.currencyfreaks.com/v2.0/supported-currencies'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Parse the JSON data
else:
    print(f"Failed to retrieve data: {response.status_code}")

#print(data)
#print(type(data))
supportedCurrencies = data['supportedCurrenciesMap']
supportedCurrenciesList = []

for currencyCode, details in supportedCurrencies.items():
    supportedCurrenciesList.append({
        'Currency Code': currencyCode,
        'Currency Name': details['currencyName'], 
        'Country Code': details['countryCode'], 
        'Country Name': details['countryName'], 
        'Status': details['status']
    })
#print(supportedCurrenciesList)

df = pd.DataFrame(supportedCurrenciesList)  
df.to_csv('supportedCurrenciesList.csv', index = False)


username = 'ifeoma' 
password = #Password of the database
host = 'localhost' 
port = '5432'  
database_name = 'CurrencyExchangeRates' 

# Create a SQLAlchemy engine 
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database_name}') 
# Load DataFrame into PostgreSQL table 
df.to_sql('supportedcurrency', engine, if_exists='replace', index=False)
