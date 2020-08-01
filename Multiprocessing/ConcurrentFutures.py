import concurrent.futures
import time

def do_something(seconds):
    print(f'Sleeping {seconds} second ...')
    time.sleep(seconds)
    return f'Done Sleeping ...{seconds}'

if __name__ == '__main__':

    start = time.perf_counter()


    # do_something()
    # do_something()

    # p1 = multiprocessing.Process(target=do_something)
    # p2 = multiprocessing.Process(target=do_something)

    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        # secs = [5,4,3,2,1]
        # results = [executor.submit(do_something, sec) for sec in secs]
        # # f1 = executor.submit(do_something, 1)
        # #         # f2 = executor.submit(do_something, 1)# submit schedules a function to be executed and returns a futures object
        # #         # # our futures object encapsulates our function allows us to check on it after it has been scheduled
        # #         # print(f1.result())
        # #         # print(f2.result())
        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())

        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

    # processes = []

    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_something, args=[1.5])
    #     p.start()
    #     processes.append(p)

    # for process in processes:
    #     process.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} seconds(s)')