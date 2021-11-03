import sys

def stock_prices(company_name):
    if len(company_name) > 2 or len(company_name) == 1 :
        return
    name = company_name[1].capitalize()
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
    if name in COMPANIES :
        print(STOCKS[COMPANIES[company_name[1].capitalize()]])
    else :
        print("Unknown company")

if __name__== '__main__':
    stock_prices(sys.argv)