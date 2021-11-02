#!/usr/bin/python3

def data_types():
    lst = [5, '', 1.1 , True, [], {}, (), set()]
    len_minus_one_lst = len(lst) - 1

    print('[', end='')
    for i in range(len(lst)):
        print(type(lst[i]).__name__, end='')
        if i < len_minus_one_lst:
            print(", ", end=' ')
    print(']')
    
if __name__ == '__main__':
    data_types()