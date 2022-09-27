import requests
import time
import secret
import json
from datetime import datetime



BITCOIN_API_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
ifttt_webhook_url = secret.COIN_API_KEY
BITCOIN_PRICE_THRESHOLD = 10000

def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL)
    response_json = response.json()
    return float(response_json[0]['price_usd'])

def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')
        price = bitcoin_price['price']
        row = '{}: $<b>{}</b>'.format(date, price)
        rows.append(row)


    return '<br>'.join(rows)

def post_ifttt_webhook(event, value):
    data = {'value1': value}
    ifttt_event_url = ifttt_webhook_url.format(event)
    requests.post(ifttt_event_url, json=data)

def main():
    BITCOIN_PRICE_THRESHOLD = 10000  # Set this to whatever you like

def main():
    bitcoin_history = []
    while True:
        price = get_latest_bitcoin_price()
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})
        if price < BITCOIN_PRICE_THRESHOLD:
            post_ifttt_webhook('bitcoin_price_emergency', price)
        if len(bitcoin_history) == 5:
            post_ifttt_webhook('bitcoin_price_update', 
                               format_bitcoin_history(bitcoin_history))
            bitcoin_history = []
        time.sleep(5 * 60)

if __name__ == "__main__":
    main()


