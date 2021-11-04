import sys

def check_for_ascii(string):
    string.encode('ascii')

def caeser(string, shift):
    result = ""
 
    # traverse string
    for i in range(len(string)):
        char = string[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif(char.islower()):
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise Exception('Error. Try python3 caesar.py encode \'ssh -i private.key user@school21.ru\' 12')
    try:
        check_for_ascii(sys.argv[2])
    except UnicodeEncodeError:
        raise Exception('The script does not support your language yet.')
    if sys.argv[1] == 'encode':
        print(caeser(sys.argv[2], int(sys.argv[3])))
    elif sys.argv[1] == 'decode':
        print(caeser(sys.argv[2], -int(sys.argv[3])))
    else:
        raise Exception('Error. The second argument must bu \'encode\' or \'decode\'')