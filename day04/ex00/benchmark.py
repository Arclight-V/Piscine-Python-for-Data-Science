#!usr/bin/python3

import timeit


def loop(email, src_emails):
    new_list_emails = []
    for elem in src_emails:
        if elem == email:
            new_list_emails.append(elem)
    return new_list_emails


def list_comprehension(email, src_emails):
    return [email for email in src_emails]


if __name__ == '__main__':
    emails = ['john@gmail.com',
              'james@gmail.com',
              'alice@yahoo.com',
              'anna@live.com',
              'philipp@gmail.com'] * 5

    number_of_repetitions = 90000000

    loop_function = 'loop(emails[5], emails)'
    comprehension_function = 'list_comprehension(emails[5], emails)'

    timeit_loop = timeit.timeit(loop_function, globals=globals(), number=number_of_repetitions)
    timeit_comprehension = timeit.timeit(loop_function, globals=globals(), number=number_of_repetitions)

    if (timeit_comprehension <= timeit_loop):
        print(f'it is better to use a list comprehension\n{timeit_comprehension} vs {timeit_loop}')
    else:
        print(f'it is better to use a loop\n{timeit_loop} vs {timeit_comprehension}')
