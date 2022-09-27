import requests
from requests import Session
import secret

# Python for API - Learn how to access any API with Python https://www.youtube.com/watch?v=p71SWzjeqtk
# Coinmarket API Docs https://coinmarketcap.com/api/documentation/v1/

#Basic test
url = secret.DOTA_KEY
ifttt_webhook_url = 'https://maker.ifttt.com/trigger/dota_discord_bot/with/key/bN4U9HGzPvet2cpT5OBzVF'

headers = {
'Accepts': 'application/json',
'X-CMC_PRO_API_KEY': secret.DOTA_KEY
 }

r = requests.get(url, headers = headers)

def post_match_id(value):
    data = {'value1' : value}


def main():
    ifttt_webhook_url = 'https://maker.ifttt.com/trigger/dota_discord_bot/with/key/bN4U9HGzPvet2cpT5OBzVF'
    requests.post(ifttt_webhook_url)

if __name__ == "__main__":
    main()