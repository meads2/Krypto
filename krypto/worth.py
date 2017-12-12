class Worth():
    api_url = 'https://api.gdax.com/'
    def __init__(self, coins={}, prices={}, account_id=[]):
        self.coins = coins
        self.prices = prices
        self.account_id = account_id

    def netWorth(self, outputres=False):
        '''
        Gets the current market value of all coins
        '''
        # Current coin holdings
        myBTC = 0
        myLTC = 0
        myETH = 0

        # Sets Coin Quanities
        coins = self.coins
        for coin in coins:
            if coin =='ETH':
                myETH = coins[coin]
            elif coin == 'LTC':
                myLTC = coins[coin]
            else:
                myBTC = coins[coin]

        # Sets Current Market Prices
        ETH_Price=0
        LTC_Price=0
        BTC_Price=0
        prices = self.prices
        for price in prices:
            if price =='ETH':
                 ETH_Price = prices[price]
            elif price == 'LTC':
                LTC_Price = prices[price]
            else:
                BTC_Price = prices[price]

        netWorth = round((myBTC * BTC_Price) + (myLTC * LTC_Price) + (myETH * ETH_Price), 2)
        if outputres==True:
            print "Current Net Worth: $%s" %netWorth
        return netWorth


    def totalInvested(self):
        '''
        Gets the sum of all money invested
        '''
        invested = []
        for id in range(len(self.account_id)):
            r = requests.get(api_url + '/accounts/' + self.account_id[id] +'/ledger', auth=auth)
            r = r.json()
        print r
            # amount= r[0]['balance']
            # invested.append(amount)
            # print amount 

        # totalInvested = sum(invested)
        # return totalInvested

    def myEarnings(self, netWorth=0, totalInvested=0, outputres=False):
        '''
        Finds the differnece between total investment 
        '''
        myEarnings = round(netWorth - totalInvested, 2)
        if outputres==True:
            print 'Your Earnings are: $%s' %myEarnings
        return myEarnings