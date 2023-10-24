'''     Example-1    '''
# from threading import Thread
# from time import sleep

# def squares(n):
#     sleep(1)
#     print('square is : ', n**2)
# def cubes(n):
#     print('cube is : ', n**3)

# t1 = Thread(target=squares, args=(3,))
# t2 = Thread(target=cubes, args=(3,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()


'''     Example-2    '''
from queue import Queue
from threading import Thread, Condition
from time import sleep


cond = Condition()
def producer(q: Queue):
    for i in range(5):
        q.put(i)
        print("producer produced: ", i)
    
def consumer(q: Queue):
    while True:
        data = q.get()
        print('consumer consumed: ', data)

q = Queue()
pro_thread = Thread(target=producer, args=(q,))
con_thread = Thread(target=consumer, args=(q,))

pro_thread.start()
con_thread.start()

pro_thread.join()
con_thread.join()

