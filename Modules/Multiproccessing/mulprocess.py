import multiprocessing
import time

start = time.perf_counter()

def random():
    print('zunzunzun')
    time.sleep(1)
    print('khatam')

if __name__ == '__main__':
    arr = []
    for _ in range(10):
        p = multiprocessing.Process(target=random)
        p.start()
        arr.append(p)

    for process in arr:
        process.join()

    finish = time.perf_counter()

    print(f"Finished in : {round(finish-start, 2)}seconds")