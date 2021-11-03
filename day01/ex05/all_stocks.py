import sys

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def pars_argv(lst):
    for elem in lst:
        if elem == '':
            return []

    new_lst = []
    for elem in lst:
        ibegin = 0
        iend = len(elem) - 1
        begin = 0
        end = 0
        while elem[ibegin] == ' ':
            begin += 1
            ibegin += 1
        while elem[iend] == ' ':
            iend -= 1
            end = iend
        while ibegin < iend:
            if elem[ibegin] == ' ':
                return []
            ibegin += 1
        if begin > 0 and end > 0:
            new_lst.append(elem[begin:end])
        elif begin == 0 and end > 0:
            new_lst.append(elem[:end + 1])
        else:
            new_lst.append(elem[begin:])
    return new_lst

def all_stocks(lst):
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
        }
    
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
        }
    tmp = ''
    tmp2 = ''
    for elem in lst:
        tmp = elem.upper()
        tmp2 = elem.lower().capitalize()
        if tmp in COMPANIES.values():
            print("{} is a ticker symbol for {}".format(tmp, get_key(COMPANIES, tmp)))
        elif tmp2 in COMPANIES.keys():
            print("{} is a ticker symbol for {}".format(tmp2, STOCKS[COMPANIES[tmp2]]))
        else:
            print("{} is an unknown company or an unknown ticker symbol".format(tmp2))
            
if __name__ == '__main__':
    if len(sys.argv) > 2 or len(sys.argv) == 1:
        print()
    else:
        lst = pars_argv(list(sys.argv[1].split(',')))
        if len(lst) > 0 :
            all_stocks(lst)
        else:
            print()