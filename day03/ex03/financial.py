import sys
import os
import time
from bs4 import BeautifulSoup
import requests


def financial(ticker_symbol, field_of_the_table):
    url = f'https://finance.yahoo.com/quote/{ticker_symbol.lower()}/financials?p={ticker_symbol.lower()}'
    req = requests.get(url, headers={'User-Agent': 'Custom'})
    time.sleep(5)
    soup = BeautifulSoup(req.text, 'html.parser')
    # Google->More Tools->Developer Tools
    income_statement = soup.find(class_="D(tbrg)")
    list_all_field = [text for text in income_statement.stripped_strings]
    i = 0
    while i < len(list_all_field):
        if list_all_field[i] == field_of_the_table:
            break
        i += 6
    if i >= len(list_all_field):
        raise Exception(f'Error! Field \'{field_of_the_table}\' not found')
    print(f'({field_of_the_table},'
          f' \'{list_all_field[i + 1]}\','
          f' \'{list_all_field[i + 2]}\','
          f' \'{list_all_field[i + 3]}\','
          f' \'{list_all_field[i + 4]}\''
          f' \'{list_all_field[i + 5]}\')')


if __name__ == '__main__':
    name_env = 'anatashi'
    red = '\033[31m'
    blue = '\033[34m'
    reset = '\033[0m'

    try:
        if os.environ['VIRTUAL_ENV'][-len(name_env):] != name_env:
            raise KeyError('VIRTUAL_ENV != {}', name_env)
        if len(sys.argv) != 3:
            raise Exception(f"Must by there should be 2 arguments: ticker symbol and the field of the table\n{blue}"
                            f"Example{reset}: financial.py 'MSFT' 'Total Revenue'")
        financial(sys.argv[1], sys.argv[2])
    except AttributeError as aerr:
        print(f'No results for \'{sys.argv[1]}\'')
    except Exception as err:
        print(f'{red}Error{reset}: {err}')
    except KeyError as kerr:
        print(f'KeyError: {kerr} is None')
