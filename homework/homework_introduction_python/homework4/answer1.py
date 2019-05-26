"""
参考答案
https://talk.pycourses.com/topic/39/python%E5%85%A5%E9%97%A8-%E4%BD%9C%E4%B8%9A-%E5%9B%9B-%E7%AD%94%E6%A1%88


1\. 使用多线程请求一定数量HTTPBIN网站页面并存储结果

要求:
- 地址格式 http://httpbin.org/get?a=X X为不同的数字
- 线程数为5
- 控制并发数量为3，使用线程池或者信号量都可以
- 使用队列1提交全部任务10个
- 使用队列2存储不同线程执行的结果
- 为了让结果随机，可以随机sleep一点点时间

```
❯ python 1.py  # 你执行的结果可能不一样
Thread1 ['1', '5', '8']
Thread0 ['0', '4', '7']
Thread2 ['2', '3', '6', '9']
```

提示：用Session提高性能
"""
import requests
import json
import threading
import queue
import collections

s = requests.session()


def req(url):
    return json.loads(s.get(url).content)["args"]


class Worker(threading.Thread):
    def __init__(self, exeq, resq):
        super().__init__()
        self._exeq = exeq
        self._resq = resq
        self.daemon = True
        self.start()

    def run(self):
        while 1:
            f, args = self._exeq.get()
            try:
                res = f(args)
                self._resq.put((self.name, res))
            except Exception as e:
                print(e)
            self._exeq.task_done()


class ThreadPool:
    def __init__(self):
        self._exeq = queue.Queue()
        self._resq = queue.Queue()
        for _ in range(3):
            Worker(self._exeq, self._resq)

    def add_task(self, f, arg):
        self._exeq.put((f, arg))

    def wait_complete(self):
        self._exeq.join()


pool = ThreadPool()
for i in range(10):
    pool.add_task(req, "http://httpbin.org/get?a=" + str(i))
pool.wait_complete()

result = collections.defaultdict(list)
while not pool._resq.empty():
    name, res = pool._resq.get()
    result[name].append(res)

print(result)
