"""
3. 使用TASK 的写法
- 抓取10个 http://httpbin.org/get?a=X 这样的url (X为0-9这十个数字)
- 使用ensure_future+gather
- 最后用异步列表解析式搜集起来
```
❯ python 3.py
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```
"""

import aiohttp
import asyncio

loop = asyncio.get_event_loop()
session = aiohttp.ClientSession(loop=loop)


async def fetch(i):
    res = await session.get("http://httpbin.org/get?a=" + str(i))
    return await res.json()


tasks = [asyncio.ensure_future(fetch(i)) for i in range(10)]
loop.run_until_complete(asyncio.wait(tasks))
result = [task.result().get("args").get("a") for task in tasks]
print(result)
loop.close()
