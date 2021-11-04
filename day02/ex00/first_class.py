class FirstClass:
    try:
        with open('data.csv', 'r') as f:
            print(f.read())
    except OSError as err:
        print(f'OS error: {err}')

if __name__ == '__main__':
    FirstClass()