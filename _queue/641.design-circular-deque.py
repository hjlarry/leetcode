#
# @lc app=leetcode id=641 lang=python3
#
# [641] Design Circular Deque
#
# https://leetcode.com/problems/design-circular-deque/description/
#
# algorithms
# Medium (49.13%)
# Likes:    103
# Dislikes: 29
# Total Accepted:    6.8K
# Total Submissions: 13.8K
# Testcase Example:  '["MyCircularDeque","insertLast","insertLast","insertFront","insertFront","getRear","isFull","deleteLast","insertFront","getFront"]\n[[3],[1],[2],[3],[4],[],[],[],[4],[]]'
#
# Design your implementation of the circular double-ended queue (deque).
#
# Your implementation should support following operations:
#
#
# MyCircularDeque(k): Constructor, set the size of the deque to be k.
# insertFront(): Adds an item at the front of Deque. Return true if the
# operation is successful.
# insertLast(): Adds an item at the rear of Deque. Return true if the operation
# is successful.
# deleteFront(): Deletes an item from the front of Deque. Return true if the
# operation is successful.
# deleteLast(): Deletes an item from the rear of Deque. Return true if the
# operation is successful.
# getFront(): Gets the front item from the Deque. If the deque is empty, return
# -1.
# getRear(): Gets the last item from Deque. If the deque is empty, return
# -1.
# isEmpty(): Checks whether Deque is empty or not.
# isFull(): Checks whether Deque is full or not.
#
#
#
#
# Example:
#
#
# MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be
# 3
# circularDeque.insertLast(1);            // return true
# circularDeque.insertLast(2);            // return true
# circularDeque.insertFront(3);            // return true
# circularDeque.insertFront(4);            // return false, the queue is full
# circularDeque.getRear();              // return 2
# circularDeque.isFull();                // return true
# circularDeque.deleteLast();            // return true
# circularDeque.insertFront(4);            // return true
# circularDeque.getFront();            // return 4
#
#
#
#
# Note:
#
#
# All values will be in the range of [0, 1000].
# The number of operations will be in the range of [1, 1000].
# Please do not use the built-in Deque library.
#
#
#
class Node:
    __slots__ = ("value", "prev_ref", "next_ref")

    def __init__(self, value=None, next_ref=None, prev_ref=None):
        self.value, self.next_ref, self.prev_ref = value, next_ref, prev_ref


# my solution , 80%
class MyCircularDeque(object):
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.max_size = k
        self.current_size = 0
        self.head = Node()
        self.tail = Node(next_ref=self.head, prev_ref=self.head)
        self.head.next_ref = self.tail
        self.head.prev_ref = self.tail

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        temp = self.head.next_ref
        new = Node(value, next_ref=temp, prev_ref=self.head)
        self.head.next_ref = new
        temp.prev_ref = new
        self.current_size += 1
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        temp = self.tail.prev_ref
        new = Node(value, next_ref=self.tail, prev_ref=temp)
        self.tail.prev_ref = new
        temp.next_ref = new
        self.current_size += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        need_del = self.head.next_ref
        need_del.next_ref.prev_ref = self.head
        self.head.next_ref = need_del.next_ref
        self.current_size -= 1
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        need_del = self.tail.prev_ref
        need_del.prev_ref.next_ref = self.tail
        self.tail.prev_ref = need_del.prev_ref
        self.current_size -= 1
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        result = self.head.next_ref.value
        if result is None:
            return -1
        return result

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        result = self.tail.prev_ref.value
        if result is None:
            return -1
        return result

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        if self.current_size == 0:
            return True
        return False

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        if self.current_size >= self.max_size:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
