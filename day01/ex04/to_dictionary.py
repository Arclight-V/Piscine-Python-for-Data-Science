def to_print_dictionary(dict):
    for key, values in dict.items():
        for value in values:
            print("'{}' : '{}'".format(key, value))

    # a similat output
    # print(*dict.items(), sep='\n')

def to_dictionary():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
        ]
    new_dict = {}
    for i in list_of_tuples:
        if i[1] in new_dict:
            new_dict[i[1]].append(i[0])
        else:
            new_dict[i[1]] = [i[0]]
    return new_dict

def to_main():
    to_print_dictionary(to_dictionary())

if __name__ == '__main__':
    to_main()