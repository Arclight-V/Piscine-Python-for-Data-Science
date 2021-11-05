import sys
import os

def financial():
    x = None

if __name__ == '__main__':
    name_env = 'anatashi'
    red = '\033[31m'
    blue = '\033[34m'
    reset = '\033[0m'

    try:
        if os.environ['VIRTUAL_ENV'][-len(name_env):] != name_env:
            raise KeyError('VIRTUAL_ENV != {}', name_env)
        if len(sys.argv) != 2:
            raise Exception(f"Must by there should be 2 arguments: ticker symbol and the field of the table\n{blue}"
                            f"Example{reset}: financial.py 'MSFT' 'Total Revenue'")
        financial()
    except Exception as err:
        print(f'{red}Arguments Error{reset}: {err}')
    except KeyError as kerr:
        print(f'KeyError: {kerr} is None')