import sys

def letter_starter(email):
    with open('employees.tsv', 'r') as file_to_read:
        for line in file_to_read:
            if line.find(email) > 0:
                t = line.find('\t')
                print(f"Dear {line[0:t]}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1].find('@corp') == -1:
        raise Exception('Error! There is no email "example.example@corp" as an argument')
    letter_starter(sys.argv[1])
