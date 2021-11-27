from links import Links
from random import randint


def test_links_init(links):
    for elem in links.id_lines_:
        print(elem)


def test_get_imdb(links):
    list_of_movies = [randint(1, 640000) for i in range(20)]
    print(list_of_movies)
    print(links.get_imdb(list_of_movies, None))


if __name__ == '__main__':
    path_to_file = './ml-latest-small/links.csv'
    links = Links(path_to_file)

    test_links_init(links)
    # test_get_imdb(links)