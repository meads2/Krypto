import requests 
from requests.auth import AuthBase
from tabulate import tabulate
    
class Holdings():

    def __init__(self, auth, product='BTC'):
        self.product = product
        self.auth = auth
        self.api_url = 'https://api.gdax.com/'

    def getAccounts(self, outputres=False):
        r = requests.get(self.api_url + 'accounts', auth=self.auth)
        r = r.json()

        # Empty array for accounts
        accounts=[]

        for account in range(len(r)):
            accounts.append(r[account]['id'])
        pprint(accounts)

        if outputres==True:
            print 'Your accounts are: %s' %accounts

        return accounts

    def curr_holdings(self):
        '''
        Returns the total balance in US dollars for an account
        '''
        r = requests.get(self.api_url + 'accounts', auth=self.auth)
        r = r.json()

        if self.product == 'BTC':
            btc = round(float(r[1]['balance']),4)
            return btc
        elif self.product == 'USD':
            usd = round(float(r[0]['balance']),4)
            return usd
        elif self.product == 'ETH':
            eth = round(float(r[2]['balance']),4)
            return eth
        else:
            ltc = round(float(r[3]['balance']),4)
            return ltc
        
    def allHoldings(self):
        r = requests.get(self.api_url + 'accounts', auth=self.auth)
        r = r.json()
        btc = str(round(float(r[1]['balance']),4))
        eth = str(round(float(r[2]['balance']),4))
        ltc = str(round(float(r[3]['balance']),4))
        usd = str(round(float(r[0]['balance']),2))

        holdings = {
            'BTC': btc,
            'ETH':eth,
            'LTC':ltc,
            'USD':usd
        }

        print "------------------------------------"
        print "-        Your GDAX Holdings        -"
        print "------------------------------------"
        print tabulate([[btc, eth, ltc, usd]], 
                        headers=['BTC', 'ETH', 'LTC', 'USD'], 
                        tablefmt='orgtbl', 
                        numalign="center", 
                        stralign="center")
        return holdings