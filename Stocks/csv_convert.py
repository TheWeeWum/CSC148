import csv

#############################################################################
# GETS INITIAL DICTIONARY TO USE FOR CALCULATIONS
#############################################################################

files = [
    'C:/Users/Liam Csiffary/PycharmProjects/CSC148/Stocks/TickerData/GOOGL.csv',
    'C:/Users/Liam Csiffary/PycharmProjects/CSC148/Stocks/TickerData/A.csv'
]
# [ticker: {date, open, high, low, close}]
tickers = []
for file in files:
    dic = {}
    with open(file, 'r') as f:
        dic['name'] = f.name
        dic['date'] = []
        dic['open'] = []
        dic['high'] = []
        dic['low'] = []
        dic['close'] = []
        reader = csv.reader(f)
        i = 0
        for row in reader:
            if i == 0:
                i = 1
                continue
            parts = row
            dic['date'].append(parts[0])
            dic['open'].append(float(parts[1]))
            dic['high'].append(float(parts[2]))
            dic['low'].append(float(parts[3]))
            dic['close'].append(float(parts[4]))
    tickers.append(dic)

# print(tickers)

#############################################################################
# INITIAL CONDITIONS
#############################################################################
initial_money = 1000000
money = initial_money
num_buy = 10
owned_stocks = {}


############
# conditions
############
def rudimentary_buy(current_price, last_price, name, money=money) -> bool:
    if current_price < last_price:
        if money > current_price * num_buy:
            money -= current_price * num_buy
            owned_stocks[name] += num_buy


def rudimentary_sell(current_price, last_price, name, money=money) -> bool:
    if current_price > last_price:
        if owned_stocks[name] > num_buy:
            money += current_price * num_buy
            owned_stocks[name] -= num_buy


def net_worth(last_price, name, num_stocks=-1):
    if num_stocks != -1:
        return num_stocks * last_price
    return money + owned_stocks[name] * last_price


for ticker in tickers:
    last_price = ticker['open'][0]
    name = ticker['name']
    owned_stocks[name] = 0
    control = initial_money / last_price
    for i in range(len(ticker['date'])):
        date = ticker['date'][i]
        opens = ticker['open'][i]
        high = ticker['high'][i]
        low = ticker['low'][i]
        close = ticker['close'][i]

        cur_p = opens
        rudimentary_sell(cur_p, last_price, name)
        rudimentary_buy(cur_p, last_price, name)
        last_price = cur_p

        cur_p = close
        rudimentary_sell(cur_p, last_price, name)
        rudimentary_buy(cur_p, last_price, name)
        last_price = cur_p

    print(name[-9:-4], 'Algo at:', net_worth(last_price, name), '   last_price:', last_price)
    print(name[-9:-4], "CONTROL:", net_worth(last_price, name, control))
