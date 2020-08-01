import multiprocessing
import time


def do_something(seconds):
    print(f'Sleeping {seconds} second ...')
    time.sleep(seconds)
    print('Done Sleeping ...')


if __name__ == '__main__':

    start = time.perf_counter()


    # do_something()
    # do_something()

    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()

    with concurrent.futures.ProcessPoolExecutor() as executor:

    processes = []

    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} seconds(s)')