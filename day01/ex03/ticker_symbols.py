import sys

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def ticker_symbols(ticker):
    if len(ticker) > 2 or len(ticker) == 1 :
        return

    ticker = ticker[1].upper()

    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    name = get_key(COMPANIES, ticker)

    if name:
        print(name, STOCKS[ticker], sep=' ')
    else:
        print("Unknown company")

if __name__ == '__main__' :
    ticker_symbols(sys.argv)