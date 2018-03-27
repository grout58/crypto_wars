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
    def __init__(self, name, price, multi, rand_multi, low):
        self.name = name
        self.price = price
        self.multi = multi
        self.rand_multi = rand_multi
        self.low = low


    def set_price(self):
        self.rand_multi = self.multi * random.randint(1, self.multi)
        self.price = self.low * self.rand_multi
        return self.price


## inventory
class Portfolio:
    def __init__(self, crypto_name, purchased_price, current_value, ammount):
        self.crypto_name = crypto_name
        self.purchased_price = purchased_price
        self.current_value = current_value
        self.ammount = ammount

    def purchase():
        pass




## sales

## market

