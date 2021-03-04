import random


    #  Variables

markets = ['Coinbase', 'eToro', 'Robinhood', 'CoinMama', 'BlockFi', 'Bisq']
crypto = ['BTC', 'ETH', 'XRP', 'BCH', 'EOS', 'ADA', 'LTC', 'USD']

map_location = 0

wallet = {
    'BTC': 1,
    'ETH': 0,
    'XRP': 0,
    'BCH': 0,
    'EOS': 0,
    'ADA': 0,
    'LTC': 0,
    'USD': 100000
}

currency_multiplier = {
    'BTC': 2,
    'ETH': 3,
    'XRP': 4,
    'BCH': 2,
    'EOS': 10,
    'ADA': 30,
    'LTC': 3
}

crypto_default_prices = {
    'BTC': 49463,
    'ETH': 1579,
    'XRP': 47,
    'BCH': 514,
    'EOS': 4,
    'ADA': 2,
    'LTC': 185
}

crypto_current_prices = {
    'BTC': 49463,
    'ETH': 1579,
    'XRP': 47,
    'BCH': 514,
    'EOS': 4,
    'ADA': 2,
    'LTC': 185
}

def set_price():
    rand_bonus_num = random.randrange(1,5)
    for crypto_default_prices_k, crypto_default_prices_v in crypto_default_prices.items():
        crypto_current_prices[crypto_default_prices_k] = rand_bonus_num * (crypto_default_prices_v * currency_multiplier[crypto_default_prices_k])


def crypto_buy():
    for k, v in crypto_current_prices.items():
        print(k,v)
    crypt_type = input('What would you like to buy? ').upper()
    crypt_amount = input('How many would you like to buy? ')
    crypt_amount = int(crypt_amount)
    crypt_total = int(crypto_current_prices[crypt_type]) * crypt_amount
    if wallet['USD'] >= crypt_total:
        confirm_buy = input(f'Are you sure you would like to buy {crypt_amount} {crypt_type} for {crypt_total}? ').upper()
        if confirm_buy == 'Y':
            wallet['USD'] = wallet['USD'] - crypt_total
            wallet[crypt_type] += crypt_amount
            print("Sold!")
            prompt()
        else:
            print("No problem have a good one")
            prompt()
        
    else:
        print('Go be poor somewhere else.')
        prompt()


    
def crypto_sell():
    for k, v in crypto_current_prices.items():
        print(k,v)
    crypt_type = input('What would you like to sell? ').upper()
    crypt_amount = input('How many would you like to sell? ')
    crypt_amount = int(crypt_amount)
    crypt_total = int(crypto_current_prices[crypt_type]) * crypt_amount
    if wallet[crypt_type] >= crypt_amount:
        confirm_sell = input(f'Are you sure you would like to sell {crypt_amount} {crypt_type} for {crypt_total}? ').upper()
        if confirm_sell == 'Y':
            wallet[crypt_type] = wallet[crypt_type] - crypt_amount
            wallet['USD'] += crypt_total
            print('Sold!')
            prompt()
        else:
            print('No problem, have a good day!')
            prompt()
        
    else:
        print(f'You do not have enough {crypt_type}')
        prompt()

def move():
    set_price()
    global map_location
    for market in markets:
        print(market)
    new_location = input("Where would you like to move to? ")
    new_location = int(new_location)
    map_location = new_location
    prompt()


def show_wallet():
    for k, v in wallet.items():
        if v != 0:
            print(f'You currently have {v} {k} in your wallet.')
    

def prompt():
    print(f'Your current location is {markets[map_location]}')
    show_wallet()
    selection = input('What would you like to do? m/b/s > ')
    if selection == 'b':
        crypto_buy()
    elif selection == 's':
        crypto_sell()
    elif selection == 'm':
        move()
    elif selection == 'show':
        show_wallet()
    else:
        print('Not a valid choice, please try again.')
        promtp()

    
    
    




    
prompt()

