import sys
import psutil
import os

def read_all_lines(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return lines

if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise Exception(f"\033[31mError!\033[0m Must by there should be 1 argument: 'file.csv'\n\033[34m"
                            f"Example\033[0m: python3 ordinary.py ratings.csv ")
    except Exception as exc:
        print(exc)
        sys.exit(-1)

    for line in read_all_lines(sys.argv[1]):
        pass

    process = psutil.Process(os.getpid())
    peak_memory = process.memory_info()[0] / (1024 * 1024 * 1024)
    user_time = process.cpu_times()[0]
    system_time = process.cpu_times()[1]

    print(f'Peak Memory Usage = {peak_memory:.3f} GB')
    print(f'User Mode Time + System Mode Time = {user_time + system_time:.2f}s')