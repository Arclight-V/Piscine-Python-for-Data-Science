import sys
    
class Research:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    # self - this is the standard name of the first argument for object methods
    def file_reader(self):
        try:
            with open(self.path_to_file, 'r') as f:
                file = f.read()
            lines = file.split('\n')
            if len(lines[0].split(',')) != 2:
                raise Exception('The correct file contains a header with two strings delimited by a comma')
            if len(lines[1:]) == 0:
                raise Exception('The file contains a incorect data')
            for line in lines[1:]:
                if line != '0,1' and line != '0,0' and line != '1,0' and line != '1,1':
                    raise Exception('The data must contain either 0 or 1')
            return file
        except OSError as err:
            print(f'OS error: {err}')
        except Exception as exc:
            print(f'Exception error: {exc}')
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception(f"Error! Must by there should be two arguments")
    file = Research(sys.argv[1]).file_reader()
    if file:
        print(file)