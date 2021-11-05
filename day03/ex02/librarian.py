import os
import shutil

def librarian(name_env):
    list_lib = ['beautifulsoup4',
                'pytest',
                ]
    pip_inst = 'pip3 install '

    os.system(pip_inst + ' '.join(list_lib))
    os.system('pip freeze > requirements.txt')

    shutil.make_archive(name_env, 'zip', name_env)


if __name__ == '__main__':
    name_env = 'anatashi'
    try:
        if os.environ['VIRTUAL_ENV'][-len(name_env):] != name_env:
            raise KeyError('VIRTUAL_ENV != {}', name_env)
        else:
            librarian(name_env)
    except KeyError as kerr:
        print(f'KeyError: {kerr} is None')