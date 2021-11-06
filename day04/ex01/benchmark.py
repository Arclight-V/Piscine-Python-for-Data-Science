#!usr/bin/python3

import timeit


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

if __name__ == '__main__':
    emails = ['john@gmail.com',
              'james@gmail.com',
              'alice@yahoo.com',
              'anna@live.com',
              'philipp@gmail.com'] * 5

    number_of_repetitions = 90000000
    atgmail = '@gmail.com'

    loop_function = 'loop(atgmail, emails)'
    comprehension_function = 'list_comprehension(atgmail, emails)'
    map_function = 'map_func(atgmail, emails)'

    timeit_loop = timeit.timeit(loop_function, globals=globals(), number=number_of_repetitions)
    timeit_comprehension = timeit.timeit(comprehension_function, globals=globals(), number=number_of_repetitions)
    timeit_map = timeit.timeit(map_function, globals=globals(), number=number_of_repetitions)

    sort_time_list = sorted([timeit_loop, timeit_comprehension, timeit_map])

    if sort_time_list[0] == timeit_loop:
        best_result = 'loop'
    elif sort_time_list[0] == timeit_comprehension:
        best_result = 'list comprehension'
    else:
        best_result = 'map'

    print(f'it is better to use {best_result}\n'
          f'{sort_time_list[0]} vs {sort_time_list[1]} vs {sort_time_list[2]}')
