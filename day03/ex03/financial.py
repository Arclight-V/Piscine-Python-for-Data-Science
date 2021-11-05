import sys

if __name__ == '__main__':
    red = '\033[31m'
    blue = '\033[34m'
    reset = '\033[0m'
    try:
        if len(sys.argv) != 2:
            raise Exception(f"Must by there should be 2 arguments: ticker symbol and the field of the table\n{blue}"
                            f"Example{reset}: financial.py 'MSFT' 'Total Revenue'")
    except Exception as err:
        print(f'{red}Arguments Error{reset}: {err}')