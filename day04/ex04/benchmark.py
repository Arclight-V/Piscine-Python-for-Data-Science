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

def ft_counter(list_random_values):
    return dict(Counter(list_random_values))

def ft_top_counter(list_random_values):
    top = 10
    return Counter(list_random_values).most_common(10)

def benchmark():
    list_random_values = [random.randint(1, 100) for i in range(1000000)]
    ft_my_top(list_random_values)
    ft_counter(list_random_values)
    ft_top_counter(list_random_values)

    ft_my_function_str = 'ft_my_function'
    ft_my_top_str = 'ft_my_top'
    ft_counter_str = 'ft_counter'
    ft_top_counter_str = 'ft_top_counter'

    setup_str = f"""
from __main__ import {ft_my_function_str}, {ft_my_top_str}, {ft_counter_str}, {ft_top_counter_str}
list_random_values = {list_random_values}

"""
    ft_my_function_timeit = f'{ft_my_function_str}(list_random_values)'
    ft_my_top_timeit = f'{ft_my_top_str}(list_random_values)'
    ft_counter_timeit = f'{ft_counter_str}(list_random_values)'
    ft_top_counter_timeit = f'{ft_top_counter_str}(list_random_values)'

    timeit1 = timeit.timeit(setup=setup_str, stmt=ft_my_function_timeit, number=1)
    timeit2 = timeit.timeit(setup=setup_str, stmt=ft_my_top_timeit, number=1)
    timeit3 = timeit.timeit(setup=setup_str, stmt=ft_counter_timeit, number=1)
    timeit4 = timeit.timeit(setup=setup_str, stmt=ft_top_counter_timeit, number=1)

    return [timeit1, timeit2, timeit3, timeit4]

if __name__ == '__main__':
    benchmark_data = benchmark()
    print(f'my function: {benchmark_data[0]}\n'
          f'Counter: {benchmark_data[1]}\n'
          f'my top: {benchmark_data[2]}\n'
          f'Counter\'s top: {benchmark_data[3]}')
