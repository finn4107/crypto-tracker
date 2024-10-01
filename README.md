# Crypto Tracker

Ein einfacher Krypto-Tracker, der die aktuellen Kurse von Bitcoin (BTC), Ethereum (ETH) und Litecoin (LTC) mit der CoinMarketCap-API abruft. Der Tracker zeigt die aktuellen Preise in USD an und aktualisiert die Daten alle 30 Sekunden. Zusätzlich wird die Veränderung in Dollar ($) und Prozent (%) angezeigt. Die Farbe der Preisanzeige ändert sich, je nachdem, ob der Kurs gestiegen (grün) oder gefallen (rot) ist.

## Funktionen
- Echtzeit-Preisabfrage von BTC, ETH und LTC in USD.
- Preisaktualisierung alle 30 Sekunden.
- Anzeige der Kursänderungen in Dollar und Prozent.
- Farben für Kursbewegungen: Grün bei steigenden Kursen, Rot bei fallenden Kursen.
- Countdown-Anzeige für die nächste Aktualisierung.

## Voraussetzungen

- Python 3.x
- Bibliothek `requests`
- Bibliothek `tkinter` (standardmäßig in Python enthalten)

## Installation

1. Klone das Repository oder lade die Dateien herunter:

    ```bash
    git clone https://github.com/finn4107/crypto-tracker
    ```

## Verwendung

1. Starte das Skript:

   ```bash
   cd crypto-tracker
   ```

    ```bash
    python crypto_tracker.py
    ```

3. Nach dem Starten des Programms wird ein Fenster geöffnet, das die aktuellen Preise für BTC, ETH und LTC anzeigt.

4. Die Preise werden alle 30 Sekunden automatisch aktualisiert. Es gibt einen Countdown, der die Zeit bis zur nächsten Aktualisierung anzeigt.

5. Der Kurswert wird in USD zusammen mit der Veränderung in Dollar und Prozent angezeigt. 

   Beispiel:

   <img width="318" alt="image" src="https://github.com/user-attachments/assets/68478f30-c392-4886-aa79-d6aab3340f2b">


