#!usr/bin/python3

import timeit
import sys

def loop(atemail, src_emails):
    new_list_emails = []
    for elem in src_emails:
        if elem.endswith(atemail):
            new_list_emails.append(elem)
    return new_list_emails


def list_comprehension(atemail, src_emails):
    return [atemail for atemail in src_emails if atemail.endswith(atemail)]


def map_func(atemail, src_emails):
    return map(lambda x: x if x.endswith(atemail) else None, src_emails)
    # return list(map(lambda x: x if x.endswith(atemail) else None, src_emails))

def filter_func(atemail, src_emails):
    return [filter(lambda x: x if x.endswith(atemail) else None, src_emails)]

def benchmark(param):
    emails = ['john@gmail.com',
          'james@gmail.com',
          'alice@yahoo.com',
          'anna@live.com',
          'philipp@gmail.com'] * 5

    atgmail = '@gmail.com'
    setup_str = f"""from __main__ import {param[0]}
emails = {emails}
atgmail = '{atgmail}'
"""
    func_to_benchmark = f'{param[0]}(atgmail, emails)'

    return timeit.timeit(setup=setup_str, stmt=func_to_benchmark, number=param[1])

def check_argv():
    red = '\033[31m'
    blue = '\033[34m'
    reset = '\033[0m'

    func_names = {'loop': 'loop',
                  'list_comprehension': 'list_comprehension',
                  'map': 'map_func',
                  'filter': 'filter_func'}

    if len(sys.argv) != 3:
        raise Exception(f"{red}Error!{reset} Must by there should be 2 arguments: 'name_cicle' and 'number of repetitions'\n{blue}"
                        f"Example{reset}: python3 benchmard.py loop 10000000")
    elif not sys.argv[2].isdigit() or int(sys.argv[2]) < 1:
        raise Exception(f"{red}Error!{reset} Second argument must by: number (int)\n{blue}"
                        f"Example{reset}: python3 benchmard.py loop 10000000")
    elif sys.argv[1] in func_names.keys():
        return [func_names[sys.argv[1]], int(sys.argv[2])]
    else:
        raise Exception(f"{red}Error!{reset} First argument must by: 'loop' or 'list_comprehension' or 'map'\n{blue}"
                        f"Example{reset}: python3 benchmard.py loop 10000000")

if __name__ == '__main__':
    try:
        print(benchmark(check_argv()))
    except Exception as exc:
        print(exc)
