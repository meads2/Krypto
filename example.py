import os
from krypto.auth import CoinbaseExchangeAuth
from krypto.holdings import Holdings
from krypto.worth import Worth
from krypto.price import Price



# Get API KEYS TO AUTHENTICATE
API_KEY = os.environ['GDAX_API_KEY']
API_SECRET = os.environ['GDAX_API_SECRET']
API_PASS = os.environ['GDAX_API_PASS']

# CREATE An AUTH OBJECT
auth = CoinbaseExchangeAuth(API_KEY, API_SECRET, API_PASS)

# Get A Price
# Available Products: 'BTC', 'ETH', 'LTC'
# @param outputres: True prints a nice message, False(Default) prints nothing

btc_price = Price('BTC').getRates(outputres=True)
eth_price = Price('ETH').getRates(outputres=True)
ltc_price = Price('LTC').getRates(outputres=True)
