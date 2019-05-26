"""
参考答案
https://talk.pycourses.com/topic/42/python%E5%85%A5%E9%97%A8-%E4%BD%9C%E4%B8%9A-%E4%BA%94-%E7%AD%94%E6%A1%88

1\. 写一个异步生成器

要求：
- 用到 async for
- 抓取10个 http://httpbin.org/get?a=X 这样的url (X为0-9这十个数字)，并打印a的值

2\. 写一个异步列表解析式

要求：把第一个题目中获得的a的值，最后用异步列表解析式搜集起来：
```
❯ python 2.py
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```
"""

import aiohttp
import asyncio

loop = asyncio.get_event_loop()
session = aiohttp.ClientSession(loop=loop)


async def arange(i):
    n = 0
    while n < i:
        yield n
        n += 1


async def fetch(i):
    res = await session.get("http://httpbin.org/get?a=" + str(i))
    return await res.json()


async def result():
    async for i in arange(10):
        res = await fetch(i)
        print(res.get("args"))
        yield res


async def main():
    res = [res.get("args").get("a") async for res in result()]
    print(res)


loop.run_until_complete(main())
loop.close()
