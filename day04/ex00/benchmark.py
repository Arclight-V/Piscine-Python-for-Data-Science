#!usr/bin/python3

import timeit


def loop(email, src_emails):
    new_list_emails = []
    for elem in src_emails:
        if elem == email:
            new_list_emails.append(elem)
    return new_list_emails


if __name__ == '__main__':
    emails = ['john@gmail.com',
              'james@gmail.com',
              'alice@yahoo.com',
              'anna@live.com',
              'philipp@gmail.com'] * 5

    number_of_repetitions = 90000000

    loop_function = 'loop(emails[5], emails)'

    print(timeit.timeit(loop_function, globals=globals(), number=number_of_repetitions))
