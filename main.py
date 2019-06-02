import bigtext
import time


def main():
    print('The current time is')
    print()
    show_time()


def show_time():
    cur_time = time.gmtime()
    bigtext.display(f'{cur_time.tm_hour}:{cur_time.tm_min}:{cur_time.tm_sec}', 2)


if __name__ == '__main__':
    main()
