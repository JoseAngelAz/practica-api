import requests

#creamos clase con su constructor que pide la clave del api de parametro
class CurrencyConverter:
    def __init__(self,api_key):
        self.api_key = api_key
        self.url = f"https://v6.exchangenerate-api.com/v6/44e71fc0304a07d11017c04/latests/"

#Definimos funcion para conseguir la conversion
def get_exchange_rate(self,from_currency,to_currency):
    response = requests.get(self.url + from_currency)
    data = response.json()
    if response.status_code == 200:
        rates = data['conversion_rates']
        return rates.get(to_currency,None)
    else:
        print(f"Error: {data['error-type']}")
        return None
