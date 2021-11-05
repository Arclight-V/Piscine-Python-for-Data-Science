class Research:
    # self - this is the standard name of the first argument for object methods
    def file_reader(self):
        try:
            with open('data.csv', 'r') as f:
                return f.read()
        except OSError as err:
            print(f'OS error: {err}')

if __name__ == '__main__':
    print(Research().file_reader())