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


async def fetch(session, url):
    async with session.get(url) as response:
        result = await response.json()
        return result.get("args").get("a")


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(10):
            url = f"http://httpbin.org/get?a={i}"
            task = asyncio.ensure_future(fetch(session, url))
            tasks.append(task)
        print(await asyncio.gather(*tasks))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
