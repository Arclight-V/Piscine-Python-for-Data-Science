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
        self.link= 1;
        self.id = 0
        split_line_by_comma = [lines.split(',') for lines in f[first_line:]]
        links = [
            [f'https://movielens.org/movies/{line[self.column_movieId]}',
             f'http://www.imdb.com/title/tt{line[self.column_imdbId]}/',
             f'https://www.themoviedb.org/movie/{line[self.column_tmdbId]}']
            for line in split_line_by_comma
        ]
        self.id_lines_ = [[[split_line_by_comma[i][j], links[i][j]] for j in range(len(split_line_by_comma[1]))] for i in range(len(split_line_by_comma))]
        self.dict_movieId = {x: y for x, y in (split_line_by_comma[0][1], links[0][1])}
        print(self.dict_movieId)


    def get_imdb(self, list_of_movies, list_of_fields):
        """
The method returns a list of lists [movieId, field1, field2, field3, ...] for the list of movies given as the argument (movieId).
        For example, [movieId, Director, Budget, Cumulative Worldwide Gross, Runtime].
        The values should be parsed from the IMDB webpages of the movies.
     Sort it by movieId descendingly.
        """

        # list_of_links = [self.id_lines_[self.column_tmdbId][self.link] for imdbId in
        #                  sorted(int(self.id_lines_[i][self.column_imdbId]) for i in list_of_movies)]

        list_of_links = self.id_lines_[193609]

        # for url in list_of_links:
        #     req = urllib.request.Request(url)
        #     req.add_header('User-Agent', 'Custom')
        #     r = urllib.request.urlopen(req)
        #     soup = BeautifulSoup(r.read(), 'html.parser')
        # # Google->More Tools->Developer Tools
        # income_statement = soup.find(class_="D(tbrg)")
        # list_all_field = [text for text in income_statement.stripped_strings]
        # i = 0
        # while i < len(list_all_field):
        #     if list_all_field[i] == field_of_the_table:
        #         break
        #     i += 6
        # if i >= len(list_all_field):
        #     raise Exception(f'Error! Field \'{field_of_the_table}\' not found')
        # print(f'({field_of_the_table},'
        #       f' \'{list_all_field[i + 1]}\','
        #       f' \'{list_all_field[i + 2]}\','
        #       f' \'{list_all_field[i + 3]}\','
        #       f' \'{list_all_field[i + 4]}\''
        #       f' \'{list_all_field[i + 5]}\')'

        # return imdb_info
        return list_of_links

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
