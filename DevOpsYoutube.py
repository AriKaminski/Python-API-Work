import requests
from requests import Session
import secret
import json
from pprint import pprint as pp

# Python for API - Learn how to access any API with Python https://www.youtube.com/watch?v=p71SWzjeqtk
# Coinmarket API Docs https://coinmarketcap.com/api/documentation/v1/

class CMC:
    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY':token,}
        self.session = Session()
        self.session.headers.update(self.headers)

    def getAllCoins(self):
        url = self.apiurl + '/v1/cryptocurrency/map'
        r = self.session.get(url)
        data = r.json()['data']
        return data

    def getPrice(self, symbol):
        url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
        parameters = {'symbol' : symbol,}
        r = self.session.get(url, params=parameters)
        data = r.json()['data']
        return data 

    def getInfo(self, symbol):
        url = self.apiurl + '/v1/cryptocurrency/info'
        parameters = {'symbol' : symbol,}
        r = self.session.get(url, params=parameters)
        rcode = r.status_code
        data = rcode, r.json()
        return data  

def main():
    cmc = CMC(secret.COIN_API_KEY)

    print('Choose API Get Method')
    print('---------------------')
    print('1 - Get All Coins')
    print('2 - Get Price of A Coin')
    print('3 - Get Info of a Coin')

    choice = input(' ')

    if(choice == '1'):
        pp(cmc.getAllCoins())
    elif(choice == '2'):
        coin = input('Enter Coin Symbol = ')
        pp(cmc.getPrice(coin))
    elif(choice == '3'):
        coin = input('Enter Coin Symbol = ')
        pp(cmc.getInfo(coin))
    else:
        print('Enter a valid option')

if __name__ == '__main__':
    main()