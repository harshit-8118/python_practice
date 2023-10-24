import asyncio
import time

'''      example-1    '''
# async def main():
#     print("hello")
#     # await time.sleep(1)   # this will not work as asyncio is newer for it.
#     await asyncio.sleep(1)
#     print("world")


# if __name__ == "__main__":
#     # print(type(main()))
#     asyncio.run(main())
#     print('program ended')




'''      example-2    '''
''' CoRoutine '''
async def waiter(n):
    await asyncio.sleep(n)
    print(f'waited for {n} seconds')

''' Synchronous '''
# async def main():
#     print(time.strftime('%X'))
#     await waiter(2)
#     await waiter(3)
#     print(time.strftime('%X'))

''' Asynchronous '''
# async def main():
#     task1 = asyncio.create_task(waiter(3))
#     task2 = asyncio.create_task(waiter(2))
#     print(time.strftime('%X'))
#     await task1
#     await task2
#     print(time.strftime('%X'))


# if __name__ == "__main__":
#     asyncio.run(main())
#     print('program ended')


'''      example-3    '''                                                            

import asyncio
import time


async def waiter(n):
    await asyncio.sleep(n)
    print(f'waited for {n} seconds')

''' Asynchronous '''
async def main():                                                
    task1 = asyncio.create_task(waiter(2))
    task2 = asyncio.create_task(waiter(3))                                                     
    print(time.strftime("%X"))
    await asyncio.sleep(3)
    print(time.strftime("%X"))

if __name__ == "__main__":
    print(type(main()))
    asyncio.run(main())

