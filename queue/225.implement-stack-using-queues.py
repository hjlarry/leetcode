#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#
# https://leetcode.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (39.45%)
# Likes:    342
# Dislikes: 427
# Total Accepted:    133.3K
# Total Submissions: 335.5K
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement the following operations of a stack using queues.
# 
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# 
# 
# Example:
# 
# 
# MyStack stack = new MyStack();
# 
# stack.push(1);
# stack.push(2);  
# stack.top();   // returns 2
# stack.pop();   // returns 2
# stack.empty(); // returns false
# 
# Notes:
# 
# 
# You must use only standard operations of a queue -- which means only push to
# back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may
# simulate a queue by using a list or deque (double-ended queue), as long as
# you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top
# operations will be called on an empty stack).
# 
# 
#
import collections
# top voted solution, 68%
# only can use the deque`s popleft method.
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = collections.deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)
        for _ in range(len(self.data) -1 ):
            self.data.append(self.data.popleft())
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.data.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.data[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not len(self.data)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

