import time

"""
6. 写一个装饰器inject，在__init__时自动给类注入参数：
```
In : class Test:
...:     @injectArguments
...:     def __init__(self, x, y, z):
...:         pass
...:     
            
In : t = Test(x=4, y=5, z=6)

In : t.x, t.y, t.z
Out: (4, 5, 6)
```
提示：修改self.__dict__
"""

print("一、 __init__的装饰器")


def injectArguments(fn):
    def wrapper(*args, **kwargs):
        args[0].__dict__.update(kwargs)
        return fn(*args, **kwargs)

    return wrapper


class Test:
    @injectArguments
    def __init__(self, x, y, z):
        pass


t = Test(x=4, y=5, z=6)
print(t.x, t.y, t.z)
print()


"""
7. 使用WITH写一个函数调用计时的上下文管理器
```
In : with Timed():
...:     sleep(2)
...:     
Cost: 2.0050339698791504
```
再改写一个调用计时的装饰器，提示，可以直接把一个with管理器转换成装饰器：
```
In : @Timed2()
...: def f():
...:     sleep(2)
...:     
         
In : f()
Cost: 2.000157356262207
```
提示：魔术方法 __enter__、__exit__，time模块、ContextDecorator
"""

print("二、 上下文管理器")


class Timed:
    def __enter__(self):
        self.t1 = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Cost:{time.time()-self.t1}")

    def __call__(self, fn):
        def wrapper():
            t1 = time.time()
            fn()
            print(f"Cost:{time.time()-t1}")

        return wrapper


with Timed():
    time.sleep(2)


@Timed()
def f():
    time.sleep(2)


f()
print()

"""
8. 实现一个类，可以完成链式调用
```
In : Seq(1, 2, 3, 4)\
...:     .map(lambda x: x * 2)\
...:     .filter(lambda x: x > 4)\
...:     .reduce(lambda x, y: x + y)
...: 
Out: 14
```
"""

print("三、 链式调用")


class Seq:
    def __init__(self, *args):
        self.data = args[0] if len(args) == 1 else args

    def map(self, args):
        number = list(map(args, self.data))
        return Seq(number)

    def filter(self, args):
        number = list(filter(args, self.data))
        return Seq(number)

    def reduce(self, args):
        from functools import reduce

        number = reduce(args, self.data)
        return Seq(number)

    def __repr__(self):
        return str(self.data)


print(
    Seq(1, 2, 3, 4)
    .map(lambda x: x * 2)
    .filter(lambda x: x > 4)
    .reduce(lambda x, y: x + y)
)

