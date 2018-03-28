import os
import random


## map and travel
class Market:
    def __init__(self, name, high, low, stock, bank=False, location=None):
        self.name = name
        self.high = high
        self.low = low
        self.stock = stock
        self.bank = bank
        self.location = location

    def populate(self):
        pass


class Crypto_Currencies:
    def __init__(self, name, multi, low, price=None, rand_multi=None):
        self.name = name
        self.multi = multi
        self.low = low
        self.rand_multi = self.multi * random.randint(1, self.multi)
        self.price = self.low * self.rand_multi
       


## wallet
class Wallet:
    def __init__(self, wallet=[]):
        self.wallet = wallet


    def show_wallet(self):
        for items in self.wallet:
            print(items.name, items.price)


## inventory
class Portfolio:
    def __init__(self, crypto_name, purchased_price, current_value, ammount, wallet = []):
        self.crypto_name = crypto_name
        self.purchased_price = purchased_price
        self.current_value = current_value
        self.ammount = ammount
        self.wallet = wallet


    def purchase(self):
        pass

    


## sales

## market

