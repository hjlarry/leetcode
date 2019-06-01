"""
3. VALIDATORMETA

有时候在实例化的时候要对一些字段做验证，我们这里就举例一个id字段吧。
```
class Subject:                                                                                                                                 
    def __init__(self. id):                                                                                                                    
        if not isinstance(id, int):                                                                                                            
            raise ValidatorError                                                                                                               
        self.id = id
class ValidatorError(Exception):                                                                                                               
    pass                                                                                                                                       
                                                                                                                                               
                                                                                                                                               
class Subject:                                                                                                                                 
    def __init__(self, id):                                                                                                                    
        if not isinstance(id, int):                                                                                                            
            raise ValidatorError('Id must be integer')                                                                                                            
        self.id = id
```
使用时，如果传入的是非数字，就会抛错：
```
In : Subject(100)
Out: <__main__.Subject instance at 0x1063b3098>  #  正常

In : Subject('a')
---------------------------------------------------------------------------
ValidatorError                            Traceback (most recent call last)
<ipython-input-9-1b77cea7e204> in <module>()
----> 1 Subject('a')

<ipython-input-4-c65313f32dab> in __init__(self, id)
      6     def __init__(self, id):
      7         if not isinstance(id, int):
----> 8             raise ValidatorError('Id must be integer')   
      9         self.id = id
     10 

ValidatorError: Id must be integer  # 抛错了
```
能不能更智能和可扩展呢？我们可以通过实现一个ValidationMeta元类，让这个类支持加一种validate_XX的方法，如果定义的话，对自动检查对应XX属性：

```
class Subject(metaclass=ValidationMeta):                                                                                                       
    def __init__(self, id):                                                                                                                    
        self.id = id                                                                                                                           
                                                                                                                                               
    def validate_id(self, value):                                                                                                              
        if not isinstance(value, int):                                                                                                         
            raise ValidatorError('Id must be integer')  
```
"""


class ValidatorError(Exception):
    pass


class ValidationMeta(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        cls.validata_methods = {}
        for key in attrs.keys():
            if key.startswith("validate"):
                k = key.split("_")[1]
                cls.validata_methods.update({k: attrs[key]})
        return type.__new__(cls, name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        obj = super().__call__(*args, **kwargs)
        for k, v in obj.__dict__.items():
            if k in cls.validata_methods:
                cls.validata_methods[k](obj, v)
        return obj


class Subject(metaclass=ValidationMeta):
    def __init__(self, id):
        self.id = id

    def validate_id(self, value):
        if not isinstance(value, int):
            raise ValidatorError("Id must be integer")


s = Subject("x")
print(s.id)
