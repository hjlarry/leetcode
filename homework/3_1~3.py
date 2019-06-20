from itertools import islice, cycle

"""
参考答案:
https://talk.pycourses.com/topic/38/python%E5%85%A5%E9%97%A8-%E4%BD%9C%E4%B8%9A-%E4%B8%89-%E7%AD%94%E6%A1%88


1. 写一个生成素数的迭代器, 能迭代小于某数值以下的素数

要求: 不要使用yield

```
# 写一个类 Prime
In : for i in Prime(30):
...:     print(i)
...:
2
3
5
7
11
13
17
19
23
29
```
"""


class Prime:
    def __init__(self, max):
        self.v = 2
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        prime = self.v
        if prime > self.max:
            raise StopIteration
        self.v += 1
        for i in range(2, self.v - 1):
            if prime % i == 0:
                return next(self)
        return prime


print("一、 生成素数的迭代器")

for i in Prime(30):
    print(i, end=" ")
print()
print()

"""
2. 写一个生成素数的生成器, 但生成一定数量之后就会停止
```
In : p = prime(3)

In : next(p)
Out: 2

In : next(p)
Out: 3

In : next(p)
Out: 5

In : next(p)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-6-aa41e7f2fa96> in <module>()
----> 1 next(p)

StopIteration:

In : list(prime(5))
Out: [2, 3, 5, 7, 11]
```

"""

print("二、 生成素数的生成器")


def prime(limit):
    prime_list = [2]
    v = 3
    while True:
        for i in prime_list:
            if v % i == 0:
                break
        else:
            if len(prime_list) <= limit:
                prime_list.append(v)
                yield v
            else:
                raise StopIteration
        v += 2


print(list(prime(5)))
print()

"""
3. 使用YIELD实现用轮转调度(ROUND-ROBIN):

轮转是一种很基础的调度算法，在业务不复杂时可以让业务逻辑达到一定的平衡

```
In : list(roundrobin('ABC', 'D', 'EF'))
Out: ['A', 'D', 'E', 'B', 'F', 'C']
```
提示：使用collections.deque/或者itertools
"""

print("三、 轮转调度")


def roundrobin(*iterables):
    num_active = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while num_active:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            num_active -= 1
            nexts = cycle(islice(nexts, num_active))


print(list(roundrobin("ABC", "D", "EF")))
