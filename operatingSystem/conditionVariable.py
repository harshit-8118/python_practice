from threading import *
import time as t

cond = Condition()
done = 1

def task(name):
    global done
    with cond:
        if done == 1:
            done = 2
            print('waiting for condition variable', name)
            cond.wait()
            print('condition met', name)
        else: 
            for i in range(5):
                print('.')
                t.sleep(1)
            print('signalling condition variable', name)
            cond.notify_all()
            print('Notification done', name)

 
if __name__ == '__main__':
    t1 = Thread(target=task, args=('t1',))
    t2 = Thread(target=task, args=('t2',))

    t1.start()
    print('jump')
    t2.start()

