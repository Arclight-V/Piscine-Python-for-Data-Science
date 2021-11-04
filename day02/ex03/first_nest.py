import sys
    
class Research:
    line_number = 0
    list = []

    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.calculations = self.Calculations()

    # self - this is the standard name of the first argument for object methods
    def file_reader(self, has_header = True):
        try:
            with open(self.path_to_file, 'r') as f:
                file = f.read()
            lines = file.split('\n')
            if has_header == True:
                if len(lines[0].split(',')) != 2:
                    raise Exception('The correct file contains a header with two strings delimited by a comma')
                if len(lines[1:]) == 0:
                    raise Exception('The file contains a incorect data')
                self.line_number = 1
            for line in lines[self.line_number:]:
                if line != '0,1' and line != '0,0' and line != '1,0' and line != '1,1':
                    raise Exception('The data must contain either 0 or 1')
                tmp = line.split(',')
                self.list.append([int(tmp[0]), int(tmp[1])])
            return self.list
        except OSError as err:
            print(f'OS error: {err}')
        except Exception as exc:
            print(f'Exception error: {exc}')
            
    class Calculations:
        def counts(self, data):
            heads = 0
            tails = 0
            for elem in data:
                if elem[0] == 1 and elem[1] == 0:
                    heads += 1
                elif elem[0] == 0 and elem[1] == 1:
                    tails += 1
            return [heads, tails]

        def fractions(self, counts):
            all = counts[0] + counts[1]
            return[counts[0] / all * 100, counts[1] / all * 100]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception(f"Error! Must by there should be two arguments")
    res = Research(sys.argv[1])
    list = res.file_reader()
    if list:
        print(list)
        counts = res.calculations.counts(list)
        print(counts[0], counts[1])
        percents = res.calculations.fractions(counts)
        print(percents[0], percents[1])
