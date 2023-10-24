import asyncio, aiohttp as http
# import aiohttp as http
import time as t
from time import strftime as t

async def fetchFromGoogle():
    url = 'https://www.google.com'
    session = http.ClientSession()
    resp = await session.get(url)
    # print(await resp.content.read()) 
    print('done')
    await session.close()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
# async def main():
#     print(t("%X"))
#     await fetchFromGoogle()
#     await fetchFromGoogle()
#     await fetchFromGoogle()
#     await fetchFromGoogle()
#     await fetchFromGoogle()
#     await fetchFromGoogle()
#     await fetchFromGoogle()
#     await fetchFromGoogle()
#     print(t("%X"))

async def main():
    print(t("%X"))
    # await asyncio.gather(
    #     fetchFromGoogle(),
    #     fetchFromGoogle(),
    #     fetchFromGoogle(),
    #     fetchFromGoogle(),
    #     fetchFromGoogle(),
    #     fetchFromGoogle(),
    #     fetchFromGoogle(),
    #     fetchFromGoogle(),
    #     fetchFromGoogle(),
    #     fetchFromGoogle(),
    #     fetchFromGoogle(),
    #     fetchFromGoogle(),
    #     fetchFromGoogle(),
    #     fetchFromGoogle()
    # )
    # or 
    await asyncio.gather(
        *[fetchFromGoogle() for _ in range(20)]
    )
    # or synchronously
    # for _ in range(20):
    #     await fetchFromGoogle()
    # await asyncio.sleep(.5)
    print(t("%X"))

if __name__ == '__main__':
    asyncio.run(main())