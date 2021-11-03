def read_from_file():
    file_to_read = open('ds.csv', 'r')
    file_to_write = open('ds.tsv', "w+")

    for line in file_to_read:
        file_to_write.write(line.replace('\",', '\"\t')\
                                .replace('false,', 'false,\t')\
                                .replace('true,', 'false,\t'))

if __name__ == '__main__':
    read_from_file()