import abc
import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent))

from linklist_adt import DoubleLinkList


"""
相关练习题：
1. 第20题 验证有效括号 https://leetcode.com/problems/valid-parentheses/
2. 第32题 最长有效括号 https://leetcode.com/problems/longest-valid-parentheses/
3. 第150题 逆波兰表达式求值 https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""


class Stack(abc.ABC):
    """栈的API"""

    @abc.abstractmethod
    def push(self, item) -> bool:
        """入栈"""
        raise NotImplementedError

    @abc.abstractmethod
    def pop(self):
        """出栈"""
        raise NotImplementedError


class ArrayStack(Stack):
    def __init__(self, max_size=32):
        self.max_size = max_size
        self.count = 0
        self.items = []

    def push(self, item):
        if self.count == self.max_size:
            return False
        self.items.append(item)
        self.count += 1
        return True

    def pop(self):
        if self.count == 0:
            return None
        item = self.items.pop()
        self.count -= 1
        return item

    def is_empty(self):
        return self.count == 0

    def peek(self):
        return self.items[self.count - 1]


class LinklistStack(Stack):
    def __init__(self, max_size=32):
        self.max_size = max_size
        self.count = 0
        self.items = DoubleLinkList()

    def push(self, item):
        if self.count == self.max_size:
            return False
        self.items.append(item)
        self.count += 1
        return True

    def pop(self):
        if self.count == 0:
            return None
        item = self.items.tail_node.value
        self.items.remove_node(self.items.tail_node)
        return item


def test_stack(st):
    st.push("aa")
    st.push("bb")
    st.push("cc")
    assert "cc" == st.pop()
    assert "bb" == st.pop()
    assert "aa" == st.pop()
    assert st.pop() is None


if __name__ == "__main__":
    st1 = ArrayStack()
    st2 = LinklistStack()
    test_stack(st1)
    test_stack(st2)
