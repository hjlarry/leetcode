"""
参考答案
https://talk.pycourses.com/topic/46/python%E8%BF%9B%E9%98%B6-%E4%BD%9C%E4%B8%9A-%E4%B8%80/2

1. CACHED_METHOD

之前已经看过cached_property的实现了，缓存了property，我们这里实现一个缓存方法的装饰器吧（实际更复杂）。

要求：
- 支持超时参数：超时后缓存失效
- 可以使用@cached_method(ttl=5)也可以使用@cached_method来装饰
效果大概这样：

```
class Subject:
    def __init__(self, id):
        print(f'Init {id}')
        self.id = id

    def __repr__(self):
        return f'<{self.__class__.__name__} id={self.id}>'

    @classmethod
    def get(cls, id):
        return cls(id)


class Review:
    def __init__(self, id):
        self.id = id

    @classmethod
    def gets(cls, review_ids):
        return [cls(id) for id in review_ids]

    @cached_method(ttl=5)
    # @cached_method
    def get_subject(self):
        return Subject.get(self.id)


reviews = Review.gets([1, 2, 3])
print(reviews[0].get_subject())
print([r.get_subject() for r in reviews])
print([r.get_subject() for r in reviews])
time.sleep(5)  # 让缓存超时
print([r.get_subject() for r in reviews])
```

执行结果这样：
```
Init 1
<Subject id=1>
Init 2  
Init 3
[<Subject id=1>, <Subject id=2>, <Subject id=3>]
[<Subject id=1>, <Subject id=2>, <Subject id=3>]
Init 1
Init 2
Init 3
[<Subject id=1>, <Subject id=2>, <Subject id=3>]
```
可以看到Init X在缓存里只会拿一次，这里使用@cached_method(ttl=5), 也就是会缓存5秒然后失效。如果只使用@cached_method：

```
class Review:
    ...
    @cached_method
    def get_subject(self):
        return Subject.get(self.id)
```       
5秒后也不会失效：
```
Init 1
<Subject id=1>
Init 2
Init 3
[<Subject id=1>, <Subject id=2>, <Subject id=3>]
[<Subject id=1>, <Subject id=2>, <Subject id=3>]
[<Subject id=1>, <Subject id=2>, <Subject id=3>]
```
"""
import time


def cached_method(ttl=None):
    cache_dict = {}

    def wrapper(fn):
        def wrap(*args, **kwargs):
            instance = args[0]
            result = cache_dict.get(id(instance))
            if result and not result["expires"]:  # 没有ttl
                result = result["value"]
            elif (
                result and result["expires"] and result["expires"] > time.time()
            ):  # 有ttl但没有过期
                result = result["value"]
            else:
                result = None

            if not result:
                result = fn(*args, **kwargs)
                expires = time.time() + ttl if ttl else None
                this_dict = {id(instance): {"value": result, "expires": expires}}
                cache_dict.update(this_dict)
            return result

        return wrap

    return wrapper


class Subject:
    def __init__(self, id):
        print(f"Init {id}")
        self.id = id

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"

    @classmethod
    def get(cls, id):
        return cls(id)


class Review:
    def __init__(self, id):
        self.id = id

    @classmethod
    def gets(cls, review_ids):
        return [cls(id) for id in review_ids]

    @cached_method(ttl=5)
    # @cached_method()  # 这里很尴尬，必须加()调用才能执行
    def get_subject(self):
        return Subject.get(self.id)


reviews = Review.gets([1, 2, 3])
print(reviews[0].get_subject())
print([r.get_subject() for r in reviews])
print([r.get_subject() for r in reviews])
time.sleep(5)  # 让缓存超时
print([r.get_subject() for r in reviews])
