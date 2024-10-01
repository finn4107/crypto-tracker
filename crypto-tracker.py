import requests
import tkinter as tk
from tkinter import ttk
import time

# Funktion, um den Preis von Kryptowährungen zu holen
def get_crypto_prices(api_key, symbols=['BTC', 'ETH', 'LTC']):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key
    }
    parameters = {
        'symbol': ','.join(symbols),
        'convert': 'USD'
    }
    
    response = requests.get(url, headers=headers, params=parameters)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Aktualisiere die Preise und GUI
def update_prices():
    global last_prices
    
    data = get_crypto_prices(api_key)
    if data:
        for symbol in ['BTC', 'ETH', 'LTC']:
            new_price = data['data'][symbol]['quote']['USD']['price']
            label = price_labels[symbol]
            old_price = last_prices.get(symbol, new_price)
            
            # Berechne die Veränderung in Dollar und Prozent
            change_dollar = new_price - old_price
            change_percent = (change_dollar / old_price) * 100 if old_price != 0 else 0
            
            # Färbe den Preis grün (wenn gestiegen) oder rot (wenn gefallen)
            if new_price > old_price:
                label.config(fg="green")
            elif new_price < old_price:
                label.config(fg="red")
            else:
                label.config(fg="black")
            
            # Setze den neuen Preis und die Veränderung in Dollar und Prozent
            label.config(text=f"{symbol}: ${new_price:.2f} ({change_dollar:+.2f}$, {change_percent:+.2f}%)")
            last_prices[symbol] = new_price

    # Setze den Countdown auf 30 Sekunden und aktualisiere den Timer
    countdown(30)

# Countdown bis zur nächsten Aktualisierung
def countdown(seconds):
    if seconds > 0:
        countdown_label.config(text=f"Nächste Aktualisierung in: {seconds}s")
        root.after(1000, countdown, seconds - 1)
    else:
        update_prices()

# Hauptfenster
root = tk.Tk()
root.title("Crypto Tracker")

# API-Schlüssel
api_key = '8128c5cc-f25e-4bfc-95c5-526b9f7a64e4'

# Letzte Preise speichern, um Veränderungen zu verfolgen
last_prices = {}

# Layout der GUI
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

price_labels = {}
for i, symbol in enumerate(['BTC', 'ETH', 'LTC']):
    # Erstelle ein Label für jede Kryptowährung mit `tk.Label`
    label = tk.Label(frame, text=f"{symbol}: Lade Daten...", font=("Arial", 14))
    label.grid(row=i, column=0, pady=5)
    price_labels[symbol] = label

# Countdown Label
countdown_label = tk.Label(frame, text="Nächste Aktualisierung in: 30s", font=("Arial", 12))
countdown_label.grid(row=3, column=0, pady=10)

# Initiale Preisaktualisierung und Countdown starten
update_prices()

# Starte die GUI
root.mainloop()
