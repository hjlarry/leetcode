"""
3\. 使用标准库内置模块写一个最简单的MAPREDUCE例子
分析一下金庸小说中，金庸最喜欢用的短句是那些？

要求：

金庸小说可以网上去找
使用停用词， https://github.com/chdd/weibo/blob/master/stopwords/中文停用词库.txt
```
❯ python 3.py
ForkPoolWorker-1 reading novels/3.txt
ForkPoolWorker-3 reading novels/2.txt
ForkPoolWorker-2 reading novels/1.txt


金庸最爱说：😉

过了一会  : count:72
拍的一声  : count:69
站起身来  : count:59
砰的一声  : count:52
韦小宝大喜 : count:50
心中大喜  : count:46
否则的话  : count:44
是了    : count:41
过不多时  : count:40
突然之间  : count:38
```

提示：codecs.open处理文件编码、multiprocessing.Pool的map方法、之前的延伸阅读链接
"""

import collections
import itertools
import multiprocessing
import operator


class SimpleMapReduce:
    def __init__(self, map_func, reduce_func, num_workers=None):
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_workers)

    def partition(self, mapped_values):
        partitioned_data = collections.defaultdict(list)
        for key, value in mapped_values:
            partitioned_data[key].append(value)
        return partitioned_data.items()

    def __call__(self, inputs, chunksize=1):
        map_responses = self.pool.map(self.map_func, inputs, chunksize=chunksize)
        partitioned_data = self.partition(itertools.chain(*map_responses))
        reduced_values = self.pool.map(self.reduce_func, partitioned_data)
        return reduced_values


def file_to_words(filename):
    print("{} reading {}".format(multiprocessing.current_process().name, filename))

    output = []
    words = []
    with open("chinese_words.txt", "rb") as d:
        for line in d:
            words.append(line.decode("gbk").strip())
    with open(filename, "rb") as f:
        for line in f:
            for word in words:
                if word in line.decode():
                    output.append((word, 1))
    return output


def count_words(item):
    word, occurences = item
    return (word, sum(occurences))


input_files = ["xiaoshuo1.txt", "xiaoshuo2.txt", "xiaoshuo3.txt"]
mapper = SimpleMapReduce(file_to_words, count_words)
word_counts = mapper(input_files)
word_counts.sort(key=operator.itemgetter(1))

print("\nTOP 20 WORDS BY FREQUENCY\n")
top20 = word_counts[-20:]
longest = max(len(word) for word, count in top20)
for word, count in top20:
    print("{word:<{len}}: {count:5}".format(len=longest + 1, word=word, count=count))
