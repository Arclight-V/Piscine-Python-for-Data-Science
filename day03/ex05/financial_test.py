import sys
import os
# import time
from bs4 import BeautifulSoup
import requests


def financial(ticker_symbol, field_of_the_table):
    url = f'https://finance.yahoo.com/quote/{ticker_symbol}/financials?p={ticker_symbol}'
    req = requests.get(url, headers={'User-Agent': 'Custom'})
    # time.sleep(5)
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
    return (field_of_the_table,
            list_all_field[i + 1],
            list_all_field[i + 2],
            list_all_field[i + 3],
            list_all_field[i + 4],
            list_all_field[1 + 5])


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
        print(financial(sys.argv[1], sys.argv[2]))
    except AttributeError as aerr:
        print(f'No results for \'{sys.argv[1]}\'')
    except Exception as err:
        print(f'{red}Error{reset}: {err}')
    except KeyError as kerr:
        print(f'KeyError: {kerr} is None')


# chek if the pytest is installed
# pip list
# example starting from command line
# pytest -v financial_test.py
def test_revenue():
    info = financial('MSFT', 'Total Revenue')
    assert info[0] == 'Total Revenue'


def test_return_tuple():
    info = financial('MSFT', 'Total Revenue')
    assert type(info) == tuple


def test_return_exception_one():
    try:
        financial('MSFT', 'To')
        assert False
    except:
        assert Exception


def test_return_exception_two():
    try:
        financial('kkkkkkkkkkkkkkkkkkkk', 'Total Revenue')
        assert False
    except:
        assert AttributeError

def test_return_exception_three():
    try:
        financial(1, 1)
        assert False
    except:
        assert AttributeError