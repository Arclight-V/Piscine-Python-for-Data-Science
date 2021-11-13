class Links:
    """
    Analyzing data from links.csv
    """

    def __init__(self, path_to_the_file, has_header=True):
        """
        Put here any fields that you think you will need.
        """

        with open(path_to_the_file, 'r') as file:
            f = file.read().splitlines()
        first_line = 1 if has_header == True else 0

        self.column_movieId = 0
        self.column_imdbId = 1
        self.column_tmdbId = 2
        split_line_by_comma = [lines.split(',') for lines in f[first_line:]]
        links = [
            [f'https://movielens.org/movies/{line[self.column_movieId]}',
             f'http://www.imdb.com/title/tt{line[self.column_imdbId]}/',
             f'https://www.themoviedb.org/movie/{line[self.column_tmdbId]}']
            for line in split_line_by_comma
        ]
        # self.id_lines = list(zip(
        #     [lines.split(',') for lines in f[first_line:]],
        #     [
        #         [f'https://movielens.org/movies/{line[self.column_movieId]}',
        #          f'http://www.imdb.com/title/tt{line[self.column_imdbId]}/',
        #          f'https://www.themoviedb.org/movie/{line[self.column_tmdbId]}']
        #         for line in
        #         split_line_by_comma]
        #     ]
        # ))

        a = [['193583', '5914996', '445030'], ['11111111', '2222222', '3333333']]
        b = [['https://movielens.org/movies/193583',
             'http://www.imdb.com/title/tt5914996/',
             'https://www.themoviedb.org/movie/445030'],
             ['https://movielens.org/movies/1111111',
              'http://www.imdb.com/title/tt2222222/',
              'https://www.themoviedb.org/movie/3333333']
             ]
        # for line in links:
        #     print(line, sep='\n')

        # self.id_lines = [[a[i][j], b[i][j]] for j in range(len(a[1])) for i in range(len(a))]

        # self.id_lines = [[[a[i][j], b[i][j]] for j in range(len(a[1]))] for i in range(len(a))]

        # self.id_lines = [[[split_line_by_comma[i][j], links[i][j]] for j in range(len(split_line_by_comma[1]))] for i in range(len(split_line_by_comma))]

        self.id_lines = [[[split_line_by_comma[i][j],
                               [[f'https://movielens.org/movies/{split_line_by_comma[i][0]}',
                                f'http://www.imdb.com/title/tt{split_line_by_comma[i][1]}/',
                                f'https://www.themoviedb.org/movie/{split_line_by_comma[i][2]}']][i][j]]
                          for j in range(len(split_line_by_comma[1]))] for i in range(len(split_line_by_comma))]

        for i in range(10):
            print(self.id_lines[i], sep='\n')


    def get_imdb(list_of_movies, list_of_fields):
        """
The method returns a list of lists [movieId, field1, field2, field3, ...] for the list of movies given as the argument (movieId).
        For example, [movieId, Director, Budget, Cumulative Worldwide Gross, Runtime].
        The values should be parsed from the IMDB webpages of the movies.
     Sort it by movieId descendingly.
        """

        return imdb_info

    def top_directors(self, n):
        """
        The method returns a dict with top-n directors where the keys are directors and 
        the values are numbers of movies created by them. Sort it by numbers descendingly.
        """
        return directors

    def most_expensive(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their budgets. Sort it by budgets descendingly.
        """
        return budgets

    def most_profitable(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the difference between cumulative worldwide gross and budget.
     Sort it by the difference descendingly.
        """
        return profits

    def longest(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their runtime. If there are more than one version â€“ choose any.
     Sort it by runtime descendingly.
        """
        return runtimes

    def top_cost_per_minute(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
the values are the budgets divided by their runtime. The budgets can be in different currencies â€“ do not pay attention to it. 
     The values should be rounded to 2 decimals. Sort it by the division descendingly.
        """
        return costs
