from config import *
from analytics import Research
import logging

def main():
    logging.info('a Research object has been created')
    res = Research(path)
    logging.info('Reading from file')
    list = res.file_reader()
    if list:
        logging.info('Calculating the counts of heads and tails')
        counts = res.calculations.counts()

        logging.info('Calculating the fractions of heads and tails')
        percents = res.calculations.fractions(counts)

        logging.info('Set new data end calculate fractions')
        logging.info('Creating random pridictions')
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
        logging.info('Save report')
        res.calculations.save_file(data, output_file_name, extension_file)
        res.send_message_to_slack(create_report, url_to_send)

if __name__ == '__main__':
    if len(path) == 0:
        Research.send_message_to_slack(not_creat_report, url_to_send)
        raise Exception(f"Error! Empty path")
    logging.basicConfig(format=logging_format, 
                        level=logging.NOTSET,
                        handlers=[logging.FileHandler(log_file)])
    main()