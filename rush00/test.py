from links import Links
import sys


def test_links_init(path_to_file):
    links = Links(path_to_file)
    # for i in range(10):
    #     print(links.id_lines[i], sep='\n')
    # for elem in links.dict:
    #     print(elem)


if __name__ == '__main__':
    path_file = './ml-latest-small/links.csv'
    test_links_init(path_file)