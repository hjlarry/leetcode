""" 
相关练习题
1. 第641题 设计一个循环双端队列 https://leetcode.com/problems/design-circular-deque/
2. 第239题 滑动窗口的最大值 https://leetcode.com/problems/sliding-window-maximum/
"""


class ArrayQueue:
    def __init__(self, maxsize):
        self.items = [None] * maxsize
        self.maxsize = maxsize
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        if len(self) >= self.maxsize:
            raise Exception("queue is full!")
        self.items[self.head % self.maxsize] = item
        self.head += 1
        return True

    def dequeue(self):
        item = self.items[self.tail % self.maxsize]
        self.tail += 1
        return item

    def __len__(self):
        return self.head - self.tail

    def size(self):
        return len(self)


def test_arrayqueue():
    a = ArrayQueue(5)
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    a.enqueue(4)
    a.enqueue(5)

    assert a.dequeue() == 1
    assert a.dequeue() == 2
    a.enqueue(6)
    # print还会显示有2，因为deque并不是删除元素
    print(a.items)


# 循环队列可以避免数据搬移
class CircularQueue:
    def __init__(self, n):
        self.items = [None] * (n + 1)
        self.n = n + 1
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        # 判断队列满的公式是总结规律得出的
        if (self.tail + 1) % self.n == self.head:
            return False
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.n
        return True

    def dequeue(self):
        if self.head == self.tail:
            return None
        item = self.items[self.head]
        self.head = (self.head + 1) % self.n
        return item


def test_circlequeue():
    a = CircularQueue(5)
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    a.enqueue(4)
    a.enqueue(5)

    assert a.dequeue() == 1
    assert a.dequeue() == 2
    a.enqueue(6)
    a.enqueue(7)
    print(a.items)
    assert a.dequeue() == 3
    a.enqueue(8)
    assert a.dequeue() == 4
    assert a.dequeue() == 5
    assert a.dequeue() == 6
    assert a.dequeue() == 7
    assert a.dequeue() == 8


if __name__ == "__main__":
    test_arrayqueue()
    test_circlequeue()
