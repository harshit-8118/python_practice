import time


def name_formatter(prefix):
    while True:
        time.sleep(1)
        name = (yield)
        print(f'{prefix} : {name}')

co = name_formatter('Cool')
print(co)
next(co)
time.sleep(5)
co.send('Harshit')
time.sleep(3)
co.send("Abhishek")
time.sleep(1)
print("hello")
co.send("Prateek")
print(id(co))
co.close()
                