import heapq
import random

from adt import MinHeap

"""
topK问题：
先建立大小为K的最小堆，然后迭代序列比较堆顶元素，大于堆顶的推入堆

heapq模块本身只提供了最小堆，若需要最大堆，网上一种方案是取值对应的负数；官方推荐的则是增加一个优先级和原数据组成一个元组
"""

# 使用标准库的最小堆
class TopK:
    def __init__(self, iterable, k):
        self.min_heap = []
        self.iterable = iterable
        self.size = k

    def push(self, item):
        if len(self.min_heap) < self.size:
            heapq.heappush(self.min_heap, item)
        else:
            if item > self.min_heap[0]:
                heapq.heapreplace(self.min_heap, item)

    def get_top_k(self):
        for item in self.iterable:
            self.push(item)
        return self.min_heap


def test_top_k():
    items = list(range(1000))
    random.shuffle(items)

    k = TopK(items, 10)
    print(k.get_top_k())


# 使用自己写的最小堆
class TopK2:
    def __init__(self, iterable, k):
        self.min_heap = MinHeap(k)
        self.iterable = iterable
        self.size = k

    def push(self, item):
        if len(self.min_heap) < self.size:
            self.min_heap.add(item)
        else:
            current_min = self.min_heap.extract()
            if item > current_min:
                current_min = item
            self.min_heap.add(current_min)

    def get_top_k(self):
        for item in self.iterable:
            self.push(item)
        return self.min_heap._elements


def test_top_k2():
    items = list(range(1000))
    random.shuffle(items)

    k = TopK2(items, 10)
    print(k.get_top_k())


if __name__ == "__main__":
    test_top_k()
    test_top_k2()
