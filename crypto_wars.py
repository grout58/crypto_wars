import crypto_wars_objects
import random

wallet = crypto_wars_objects.Wallet()

coins = []

def add_currency():
    currencies = ['btc', 'eth', 'ltc']
    for i in currencies:
        if i == 'btc':
            multi = 10
            low = 100
        if i == 'eth':
            multi = 5
            low = 50
        if i == 'ltc':
            multi = 2
            low = 25

        i = crypto_wars_objects.Crypto_Currencies(i.upper(), multi, low)
        coins.append(i)

add_currency()
for i in coins:
    print(i.name, i.price)
