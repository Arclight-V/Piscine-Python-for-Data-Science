import os

def librarian():
    list_lib = ['beautifulsoup4',
                'pytest']
    #
    # print (' '.join(list_lib))

if __name__ == '__main__':
    name_env = 'anatashi'
    try:
        if os.environ['VIRTUAL_ENV'][-len(name_env):] != name_env:
            raise KeyError('VIRTUAL_ENV != {}', name_env)
        else:
            librarian()
    except KeyError as kerr:
        print(f'KeyError: {kerr} is None')
