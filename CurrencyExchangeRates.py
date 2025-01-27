import requests
import pandas as pd
from sqlalchemy import create_engine

def baseCurrency(currency):
    apikey = #API KEY
    url = f'https://api.currencyfreaks.com/v2.0/rates/latest?apikey={apikey}&base={currency}'
    response = requests.get(url)
    data = response.json() 
    return data

curr = baseCurrency('USD')
#print(curr)

rates = curr.get('rates')
#print(rates)

ratesList = []
for code,numbers in rates.items():
    ratesList.append((code,numbers))
    #print(code,':' ,numbers)
    #print('-'*20)

#print(ratesList)

#create the csv files
df = pd.DataFrame(ratesList, columns=['Currency', 'ExchangeRateInUSD'])  
df.to_csv("currencyExchangeRatesList.csv", index=False)


username = 'ifeoma' 
password = #Passowrd of the database
host = 'localhost' 
port = '5432'  
database_name = 'CurrencyExchangeRates' 

# Create a SQLAlchemy engine 
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database_name}') 
# Load DataFrame into PostgreSQL table 
df.to_sql('CurrencyexchangeRates', engine, if_exists='replace', index=False)
