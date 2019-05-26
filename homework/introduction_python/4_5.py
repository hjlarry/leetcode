"""
5\. 使用THREADPOOLEXECUTOR和多线程搭配

要求：
- 用一个线程监视当然已完成的进度
- 用ThreadPoolExecutor创建3个线程执行fib函数
- 用另外一个线程作为生产者
```
❯ python 5.py
fib(26) = 121393
fib(28) = 317811
fib(27) = 196418
fib(29) = 514229
fib(31) = 1346269
fib(30) = 832040
```

提示：使用submit方法提交新的任务
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import queue

q = queue.Queue()


def producer():
    for n in range(25, 35):
        q.put((fib, n))


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


t = threading.Thread(target=producer)
t.start()
executor = ThreadPoolExecutor(max_workers=3)
future_to_num = {}
while not q.empty():
    func, arg = q.get()
    future_to_num[executor.submit(func, arg)] = arg

for future in as_completed(future_to_num):
    num = future_to_num[future]
    try:
        result = future.result()
    except Exception as e:
        print(f"raise an exception: {e}")
    else:
        print(f"fib({num}) = {result}")
