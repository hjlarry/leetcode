"""
4\. 写一个生产者/消费者例子

要求:

- 地址格式 http://httpbin.org/get?a=X X为不同的数字
- 消费时，如果请求超时(1秒)，把未完成的任务放回队列
- 一开始先生产5个任务，任务开始的1秒后再放入剩下的5个任务
- 程序可以自动结束

```
❯ python 4.py
producing 4
producing 24
producing 71
producing 21
producing 27
consuming 4...
consuming 24...
producing 82
producing 18
producing 99
producing 28
producing 74
Put back: 24
consuming 71...
consuming 21...
consuming 27...
Put back: 27
consuming 82...
consuming 18...
consuming 99...
Put back: 99
consuming 28...
consuming 74...
consuming 24...
consuming 27...
consuming 99...
['4', '71', '21', '82', '18', '28', '74', '24', '27', '99']
```
"""

import aiohttp
import asyncio
import random

loop = asyncio.get_event_loop()
session = aiohttp.ClientSession(loop=loop)


async def fetch(i):
    res = await session.get("http://httpbin.org/get?a=" + str(i))
    return await res.json()


async def _produce(queue):
    for num in random.sample(range(100), 5):
        print("producing {}".format(num))
        item = (num, num)
        await queue.put(item)


async def produce(queue):
    await _produce(queue)
    await asyncio.sleep(1)
    await _produce(queue)


async def consume(queue):
    while 1:
        item = await queue.get()
        num = item[0]
        try:
            rs = await fetch(num)
            print("consuming {}...".format(rs))
        except aiohttp.client_exceptions.ClientConnectorError:
            print("back time too long")
            await queue.put((num, num))
        queue.task_done()


async def run():
    queue = asyncio.PriorityQueue()
    consumer = asyncio.ensure_future(consume(queue))
    await produce(queue)
    await queue.join()
    consumer.cancel()


loop.run_until_complete(run())
loop.close()
