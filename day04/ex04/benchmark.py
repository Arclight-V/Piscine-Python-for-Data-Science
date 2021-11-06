#!usr/bin/python3

import timeit
import random
from collections import Counter


def ft_my_function(list_random_values):
    dict_counts = {}

    for i in list_random_values:
        if i not in dict_counts:
            dict_counts[i] = 1
        else:
            dict_counts[i] += 1

    return dict_counts

def ft_my_top(list_random_values):
    top = 10
    return sorted(ft_my_function(list_random_values).items(), key=lambda item: -item[1])[:top]

def benchmark():
    list_random_values = [random.randint(1, 100) for i in range(1000000)]
    print(ft_my_top(list_random_values))

    # number_of_sum = param[2]
    # setup_str = f"""from __main__ import {param[0]}"""
    # func_to_benchmark = f'{param[0]}({number_of_sum})'
    #
    # return timeit.timeit(setup=setup_str, stmt=func_to_benchmark, number=param[1])

if __name__ == '__main__':
    benchmark_data = benchmark()
    print(f'my function: {benchmark_data[0]}\n'
          f'Counter: {benchmark_data[1]}\n'
          f'my top: {benchmark_data[2]}\n'
          f'Counter\'s top: {benchmark_data[3]}')
