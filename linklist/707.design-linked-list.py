#
# @lc app=leetcode id=707 lang=python
#
# [707] Design Linked List
#
# https://leetcode.com/problems/design-linked-list/description/
#
# algorithms
# Easy (22.89%)
# Likes:    327
# Dislikes: 370
# Total Accepted:    29.6K
# Total Submissions: 138.7K
# Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n[[],[1],[3],[1,2],[1],[1],[1]]'
#
# Design your implementation of the linked list. You can choose to use the
# singly linked list or the doubly linked list. A node in a singly linked list
# should have two attributes: val and next. val is the value of the current
# node, and next is a pointer/reference to the next node. If you want to use
# the doubly linked list, you will need one more attribute prev to indicate the
# previous node in the linked list. Assume all nodes in the linked list are
# 0-indexed.
#
# Implement these functions in your linked list class:
#
#
# get(index) : Get the value of the index-th node in the linked list. If the
# index is invalid, return -1.
# addAtHead(val) : Add a node of value val before the first element of the
# linked list. After the insertion, the new node will be the first node of the
# linked list.
# addAtTail(val) : Append a node of value val to the last element of the linked
# list.
# addAtIndex(index, val) : Add a node of value val before the index-th node in
# the linked list. If index equals to the length of linked list, the node will
# be appended to the end of linked list. If index is greater than the length,
# the node will not be inserted. If index is negative, the node will be
# inserted at the head of the list.
# deleteAtIndex(index) : Delete the index-th node in the linked list, if the
# index is valid.
#
#
# Example:
#
#
# MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
# linkedList.get(1);            // returns 2
# linkedList.deleteAtIndex(1);  // now the linked list is 1->3
# linkedList.get(1);            // returns 3
#
#
# Note:
#
#
# All values will be in the range of [1, 1000].
# The number of operations will be in the range of [1, 1000].
# Please do not use the built-in LinkedList library.
#
#
#
class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next, self.prev = next, prev


# a voted solution, only 7%
class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(-1)
        self.root.next = self.root.prev = self.root

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0:
            return -1
        i = 0
        current = self.root.next
        while i < index and current != self.root:
            current = current.next
            i += 1
        return current.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.root.next.prev = self.root.next = Node(val, self.root.next, self.root)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.root.prev.next = self.root.prev = Node(val, self.root, self.root.prev)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        index = max(0, index)
        i = 0
        current = self.root.next
        while i < index and current != self.root:
            current = current.next
            i += 1
        if current != self.root or i == index:
            current.prev.next = current.prev = Node(val, current, current.prev)

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0:
            return
        i = 0
        current = self.root.next
        while i < index and current != self.root:
            current = current.next
            i += 1
        if current != self.root:
            current.prev.next = current.next
            current.next.prev = current.prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

