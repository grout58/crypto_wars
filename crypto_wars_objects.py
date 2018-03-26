import os


## map and travel
class Market:
    def __init__(self, name, high, low, stock, bank='No', location = None):
        self.name = name
        self.high = high
        self.low = low
        self.stock = stock
        self.bank = bank
        self.location = location

    def populate(self):


class Crypto_Currencies:
    def __init__(self, name, high, low):
        self.name = name
        self.high = high
        self.low = low


## inventory
class Portfolio:
    def __init__(self, crypto_name, purchased_price, current_value, ammount):
        self.crypto_name = crypto_name
        self.purchased_price = purchased_price
        self.current_value = current_value
        self.ammount = ammount

    def purchase():




## sales

## market
coinbase = Market('Coinbase', 'BTC', 'LTC', False, 1)
print(coinbase.location)
