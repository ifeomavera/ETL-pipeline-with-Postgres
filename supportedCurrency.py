import requests
import pandas as pd

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

