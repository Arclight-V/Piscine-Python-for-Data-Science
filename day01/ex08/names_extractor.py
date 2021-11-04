import sys

def names_extractor(file):
    file_to_read = open(file, 'r')
    file_to_write = open("employees.tsv", "w+")
    
    file_to_write.write(f"Name\tSurname\tE-mail\n")

    dot = 0
    at = 0
    for line in file_to_read:
        dot = line.find('.')
        at = line.find('@')
        file_to_write.write(f"{line[:dot].capitalize()}\t{line[dot + 1:at].capitalize()}\t{line}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('Error! There is no file to read as an argument\n')
    names_extractor(sys.argv[1])
