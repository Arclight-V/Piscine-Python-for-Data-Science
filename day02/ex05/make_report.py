from config import *
from analytics import Research

def main():
    res = Research(path)
    list = res.file_reader()
    if list:
        counts = res.calculations.counts()

        percents = res.calculations.fractions(counts)

        res.calculations.data = res.calculations.predict_random(num_steps)
        rand_count = res.calculations.counts()

        data = template_text.format(
            len(list),
            counts[1],
            counts[0],
            percents[1],
            percents[0],
            num_steps,
            rand_count[1],
            rand_count[0]
        )
        res.calculations.save_file(data, output_file_name, extension_file)

if __name__ == '__main__':
    if len(path) == 0:
        raise Exception(f"Error! Empty path")
    main()