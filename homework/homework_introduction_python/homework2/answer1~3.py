import re


"""
参考答案
https://talk.pycourses.com/topic/33/python%E5%85%A5%E9%97%A8-%E4%BD%9C%E4%B8%9A-%E4%BA%8C-%E7%AD%94%E6%A1%88


1. 写一个匹配URL的正则表达式
支持如 www.google.com、http://www.example/file.html https://douban.com/tag 等URL的匹配

2. 写一个匹配IP地址的正则表达式
支持如 192.168.0.1，8.8.8.8 等IP地址的匹配

3. 写3个正则表达式，完成下面三个例子：
- 把字符串 2018-01-01 用正则转化成 01/01/2018
- 实现一个函数，把 CamelCase 字符串 用正则转化成 camel_case
- 在slack中，存在uid和id的对应关系，如下面的变量 ID_NAMES 。通过Slack的API能获取聊天记录，但是内容用的是uid，请用正则表达式re.sub函数实现uid和id的转换
```
ID_NAMES = {'U1EAT8MG9': 'xiaoming', 'U0K1MF23Z': 'laolin'}

s = '<@U1EAT8MG9>, <@U0K1MF23Z> 嗯 确实是这样的'
```
提示:re.sub函数第二个参数是一个pattern，不仅可以是一个正则表达式，还可以是一个函数！
"""
print("一、 正则匹配网址")
exp = re.compile(
    r"""^(https?:\/\/)?
                  ([\da-z\.-]+)
                  \.([a-z\.]{2,6})
                  ([\/\w \.-]*)\/?$
                  """,
    re.X,
)

print(exp.match("www.google.com"))
print(exp.match("http://www.example/file.html"))
print(exp.match("https://douban.com/tag"))
print(exp.match("tag/ss"))
print()

print("二、 正则匹配IP")
s0_255 = "(25[0-5]|2[0-4]\d|1\d{2}|\d{1,2})"
s_ip = re.compile(s0_255 + "\." + s0_255 + "\." + s0_255 + "\." + s0_255)
print(s_ip.match("192.168.0.1"))
print(s_ip.match("8.8.8.8"))
print(s_ip.match("256.0.0.0"))
print()

print("三、 把字符串 2018-01-01 用正则转化成 01/01/2018")
date = re.match(
    "(?P<year>\d{4})\-(?P<month>1[012]|0\d)\-(?P<day>[0-2]\d|3[01])", "2018-05-31"
).groupdict()
print("{}/{}/{}".format(date["month"], date["day"], date["year"]))
print()


print("四、把 CamelCase 字符串 用正则转化成 camel_case")


def convert(s):
    s = re.findall("([A-Z][a-z]*)", s)
    s = [word.lower() for word in s]
    return "_".join(s)


print(convert("HowToCOnvertWords"))
print()


print("五、uid和id的对应关系")
ID_NAMES = {"U1EAT8MG9": "xiaoming", "U0K1MF23Z": "laolin"}
s = "<@U1EAT8MG9>, <@U0K1MF23Z> 嗯 确实是这样的"


def search_uid():
    return "|".join(dict.fromkeys(ID_NAMES))


def match(ma):
    return ID_NAMES[ma.group()]


res = re.sub(search_uid(), match, s)
print(res)

