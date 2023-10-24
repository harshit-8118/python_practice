from multiprocessing import Process
from time import sleep

def fun(num = 2):
    # for j in range(100000): pass
    print(num ** 2)


if __name__ == "__main__":
    procs = []
    for i in range(5):
        procs.append(Process(target=fun, args=(i + 1, )))

    # print(procs)
    for proc in procs:
        proc.start()

    sleep(.11)
    print('hi')
    for proc in procs:
        proc.join()