import requests


class Price():
    '''
        A helper class to create a new price obj of current rates for
        a specific product
    '''
    def __init__(self, product):
        self.product = product

    
    def getRates(self, outputres=False):
        r = requests.get(api_url + 'products/' + self.product + '-USD/ticker')
        r = r.json()
        price = round(float(r['price']), 2)
        
        if outputres==True:
            print "-----------------------------------------"
            print "Current " + self.product +  " Price:         $%s" % price
            print "-----------------------------------------"

        return price

    def getHistorical(self):
        '''
        Gets historical data for a specific crypto product
        '''
        pass

    def predictPrice(self):
        '''
        Predict a price for a certain future time using a 
        Machine learning algorithim
        '''
        pass