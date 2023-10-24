from threading import *
import time as t
import sys
sys.stdout = open('output.txt', 'w')

# sem = Semaphore(1)
# sem = Semaphore(2)
sem = Semaphore(3)

def task(name, times = 5):
    sem.acquire()
    for i in range(times):
        print('{} working'.format(name))
        t.sleep(1)
    sem.release()


if __name__ == '__main__':
    t1 = Thread(target=task, args=('Thread-1', 2, ))
    t2 = Thread(target=task, args=('Thread-2', 2, ))
    t3 = Thread(target=task, args=('Thread-3', 4, ))
    t4 = Thread(target=task, args=('Thread-4', 1, ))
    t5 = Thread(target=task, args=('Thread-5', 5, ))
    t6 = Thread(target=task, args=('Thread-6', 6, ))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()