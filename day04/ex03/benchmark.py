#!usr/bin/python3

import timeit
import sys
from functools import reduce


def ft_loop(number_of_sum):
    sum = 0
    for i in range(1 ,number_of_sum):
        sum += i ** 2
    return i

def ft_reduce(number_of_sum):
    return reduce(lambda sum, i: sum + i ** 2, range(1, number_of_sum))

def benchmark(param):
    number_of_sum = param[2]
    setup_str = f"""from __main__ import {param[0]}"""
    func_to_benchmark = f'{param[0]}({number_of_sum})'

    return timeit.timeit(setup=setup_str, stmt=func_to_benchmark, number=param[1])


def check_argv():
    red = '\033[31m'
    blue = '\033[34m'
    reset = '\033[0m'

    func_names = {'loop' : 'ft_loop',
                  'reduce' : 'ft_reduce'
                  }

    if len(sys.argv) != 4:
        raise Exception(f"{red}Error!{reset} Must by there should be 3 arguments: 'name_cicle' 'number of repetitions' 'number for the sum of the calculation of squares' \n{blue}"
                        f"Example{reset}: python3 benchmard.py loop 10000000 5")
    elif not sys.argv[2].isdigit() or int(sys.argv[2]) < 1 or not sys.argv[3].isdigit() or int(sys.argv[3]) < 1:
        raise Exception(f"{red}Error!{reset} Second and third argument must by: number (int)\n{blue}"
                        f"Example{reset}: python3 benchmard.py loop 10000000 5")
    elif sys.argv[1] in func_names.keys():
        return [func_names[sys.argv[1]], int(sys.argv[2]), int(sys.argv[3])]
    else:
        raise Exception(f"{red}Error!{reset} First argument must by: 'loop' or 'reduce'\n{blue}"
                        f"Example{reset}: python3 benchmard.py loop 10000000")

if __name__ == '__main__':
    try:
        print(benchmark(check_argv()))
    except Exception as exc:
        print(exc)
