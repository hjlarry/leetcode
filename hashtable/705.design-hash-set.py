#
# @lc app=leetcode id=705 lang=python
#
# [705] Design HashSet
#
# https://leetcode.com/problems/design-hashset/description/
#
# algorithms
# Easy (50.12%)
# Likes:    148
# Dislikes: 39
# Total Accepted:    24.3K
# Total Submissions: 44.4K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
#
# Design a HashSet without using any built-in hash table libraries.
#
# To be specific, your design should include these functions:
#
#
# add(value): Insert a value into the HashSet.
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in
# the HashSet, do nothing.
#
#
#
# Example:
#
#
# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);
# hashSet.add(2);
# hashSet.contains(1);    // returns true
# hashSet.contains(3);    // returns false (not found)
# hashSet.add(2);
# hashSet.contains(2);    // returns true
# hashSet.remove(2);
# hashSet.contains(2);    // returns false (already removed)
#
#
#
# Note:
#
#
# All values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashSet library.
#
#
#
# the build in set, 87%
# class MyHashSet(object):
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.items = set()

#     def add(self, key):
#         """
#         :type key: int
#         :rtype: None
#         """
#         self.items.add(key)

#     def remove(self, key):
#         """
#         :type key: int
#         :rtype: None
#         """
#         try:
#             self.items.remove(key)
#         except KeyError:
#             pass

#     def contains(self, key):
#         """
#         Returns true if this set contains the specified element
#         :type key: int
#         :rtype: bool
#         """
#         return key in self.items

# my solution 63%
# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.next = None


# class MyHashSet(object):
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.m = 1024
#         self.items = [None] * self.m

#     def hash(self, key):
#         return key % self.m

#     def add(self, key):
#         """
#         :type key: int
#         :rtype: None
#         """
#         old = self.items[self.hash(key)]
#         if old is None:
#             self.items[self.hash(key)] = Node(key)
#             return
#         while old is not None:
#             if old.key == key:
#                 return
#             if old.next is None:
#                 break
#             old = old.next
#         old.next = Node(key)

#     def remove(self, key):
#         """
#         :type key: int
#         :rtype: None
#         """
#         node = self.items[self.hash(key)]
#         while node is not None:
#             if node.key == key:
#                 node.key = None
#                 return
#             node = node.next

#     def contains(self, key):
#         """
#         Returns true if this set contains the specified element
#         :type key: int
#         :rtype: bool
#         """
#         node = self.items[self.hash(key)]
#         while node is not None:
#             if node.key == key:
#                 return True
#             node = node.next
#         return False


# voted solution, 60%
class MyHashSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1024
        self.items = [None] * self.m

    def hash(self, key):
        return key % self.m

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            return
        hash_key = self.hash(key)
        if not self.items[hash_key]:
            self.items[hash_key] = []
        self.items[hash_key].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if not self.contains(key):
            return
        self.items[self.hash(key)].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hash_key = self.hash(key)
        if not self.items[hash_key]:
            return False
        for k in self.items[hash_key]:
            if k == key:
                return True
        return False
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

