import requests
import pandas as pd

def baseCurrency(currency):
    apikey = 'f9b12587d0dc4137a5480904e3513f0c'
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

df = pd.DataFrame(ratesList, columns=['Currency', 'ExchangeRateInUSD'])  
df.to_csv("currencyExchangeRatesList.csv", index=False)

