#
# @lc app=leetcode id=225 lang=python
#
# [225] Implement Stack using Queues
#

# my solution, 76%
# from collections import deque
# class MyStack(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.master = deque()
#         self.slave = deque()
        

#     def push(self, x):
#         """
#         Push element x onto stack.
#         :type x: int
#         :rtype: None
#         """
#         while len(self.master):
#             self.slave.appendleft(self.master.pop())
#         self.master.appendleft(x)
#         while len(self.slave):
#             self.master.appendleft(self.slave.pop())

#     def pop(self):
#         """
#         Removes the element on top of the stack and returns that element.
#         :rtype: int
#         """
#         return self.master.pop()
        

#     def top(self):
#         """
#         Get the top element.
#         :rtype: int
#         """
#         return self.master[-1]
        

#     def empty(self):
#         """
#         Returns whether the stack is empty.
#         :rtype: bool
#         """
#         return not len(self.master)
        

# top voted solution, 54%
from collections import deque
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = deque()


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.items.append(x)
        for _ in range(len(self.items)-1):
            self.items.append(self.items.popleft())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.items.popleft()
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.items[0]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not len(self.items)
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

