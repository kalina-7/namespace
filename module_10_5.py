from multiprocessing import Pool
import datetime


def read_info(name):
    all_data = []
    file = open(name, 'r')
    while True:
        content = file.readline()
        all_data.append(content)
        if not content:
            break
    file.close()


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':

    '''Линейный вызов'''

    start_time_1 = datetime.datetime.now()

    for filename in filenames:
        read_info(filename)

    stop_time_1 = datetime.datetime.now()

    print(f'{stop_time_1 - start_time_1} (линейный)')


    '''Многопроцессный вызов'''

    start_time_2 = datetime.datetime.now()

    with Pool(len(filenames)) as p:
        p.map(read_info, filenames)

    stop_time_2 = datetime.datetime.now()
    print(f'{stop_time_2 - start_time_2} (многопроцессный)')