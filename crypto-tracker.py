import requests
import json

def get_crypto_prices(api_key, symbols=['BTC', 'ETH', 'LTC']):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    
    # Header mit API-Schlüssel
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key
    }
    
    # Parameter für die Anfrage: welche Währungen wir haben wollen
    parameters = {
        'symbol': ','.join(symbols),
        'convert': 'USD'  # Kurs in USD
    }
    
    # API Anfrage senden
    response = requests.get(url, headers=headers, params=parameters)
    
    # Überprüfen, ob die Anfrage erfolgreich war
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Fehler bei der Anfrage: {response.status_code}")
        return None

# API-Key von CoinMarketCap
api_key = ''

# Abrufen der aktuellen Preise für BTC, ETH und LTC
prices = get_crypto_prices(api_key)

if prices:
    for symbol in ['BTC', 'ETH', 'LTC']:
        price = prices['data'][symbol]['quote']['USD']['price']
        print(f"Der aktuelle Preis von {symbol} ist: ${price:.2f}")
