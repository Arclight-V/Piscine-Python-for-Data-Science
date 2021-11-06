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

    timeit_loop = timeit.timeit(loop_function, globals=globals(), number=number_of_repetitions)
    timeit_comprehension = timeit.timeit(loop_function, globals=globals(), number=number_of_repetitions)

    if timeit_comprehension <= timeit_loop:
        print(f'it is better to use a list comprehension\n{timeit_comprehension} vs {timeit_loop}')
    else:
        print(f'it is better to use a loop\n{timeit_loop} vs {timeit_comprehension}')
