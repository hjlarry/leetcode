"""
4. 使用描述符自动设置/删除数据库对应内容

使用ORM后，创建/更新/删除数据库记录非常方便。当然我们还没有说到，就看一个效果：

```
class Article(BaseMixin, CommentMixin, SquareCoverMixin, db.Model):                                                                                                                                                                                                                                                                                                               
    author_id = db.Column(db.Integer)                                                                                                          
    cover_id = db.Column(db.String(20), default='')
```
这表示Article表，包含了字段author_id和cover_id。文章全文content字段是不合适存进数据库的，可以存入一个k-v数据库，比如Redis(存在其他数据库如memcache也可以）。通过描述符实现这样的效果：

```
class Article(BaseMixin, CommentMixin, SquareCoverMixin, PropsMixin, db.Model):                                                                                                                                                                                                                                                                                                               
    author_id = db.Column(db.Integer)                                                                                                          
    cover_id = db.Column(db.String(20), default='')
    content = PropsItem('content', '') 
```
添加了PropsMixin和PropsItem。当然作为作业来说，去掉ORM，简化一下：
```
class Article(PropsMixin):                                                                                                                                                                                                                                                                                                          
    content = PropsItem('content', '')  # 字段名字, 默认值
    def __init__(self. id):
        self.id = id    
``` 
假设现在操作id为10001的Article，可以这样：

```
article = Article(10001)
article.content  # 返回默认的空，因为还没有设置正文
article.content = '这是正文'  # 在数据库里面存了id为10001的Article的文本
article = Article(10001)
article.content  # 会返回Redis数据库存的正文内容，多次请求使用本地缓存，不再请求数据库
del article.content  # 删除对应数据库中id为10001的Article的文本
article.content  # 返回空
```
"""


class PropsMixin:
    pass


class PropsItem:
    def __init__(self, field_name, default_value):
        self.field_name = field_name
        self.default_value = default_value
        self.cache_dict = {}

    def __get__(self, instance, owner):
        if instance.id in self.cache_dict:
            return self.cache_dict[instance.id]
        return self.default_value

    def __set__(self, instance, value):
        self.cache_dict[instance.id] = value

    def __delete__(self, instance):
        self.cache_dict.pop(instance.id)


class Article(PropsMixin):
    content = PropsItem("content", "")  # 字段名字, 默认值

    def __init__(self, id):
        self.id = id


article = Article(10001)
print(article.content)  # 返回默认的空，因为还没有设置正文
article.content = "这是正文"  # 在数据库里面存了id为10001的Article的文本
article = Article(10001)
print(article.content)  # 会返回Redis数据库存的正文内容，多次请求使用本地缓存，不再请求数据库
del article.content  # 删除对应数据库中id为10001的Article的文本
print(article.content)  # 返回空
