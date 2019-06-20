"""
4\. 使用多进程模块写一个使用优先级队列的例子
```
❯ python 4.py
put :7
put :36
put :91
put :10
put :73
put :23
[PRI:7] 7 * 2 = 14
[PRI:10] 10 * 2 = 20
[PRI:23] 23 * 2 = 46
[PRI:36] 36 * 2 = 72
[PRI:73] 73 * 2 = 146
[PRI:91] 91 * 2 = 182
```
提示：用BaseManager共享queue.PriorityQueue
"""

# Server side
from multiprocessing.managers import BaseManager
import queue
import random

host = "127.0.0.1"
port = 9030
authkey = b"secret"

tasks_queue = queue.PriorityQueue()


class RemoteManager(BaseManager):
    pass


def double(n):
    return n * 2


RemoteManager.register("get_queue", callable=lambda: tasks_queue)
mgr = RemoteManager(address=(host, port), authkey=authkey)
mgr.start()
tasks_queue = mgr.get_queue()
count = 0
while 1:
    if count < 5:
        pri = random.randint(1, 100)
        print(f"put :{pri}")
        tasks_queue.put((pri, double, pri))
        count += 1
