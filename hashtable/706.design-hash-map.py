#
# @lc app=leetcode id=706 lang=python
#
# [706] Design HashMap
#
# https://leetcode.com/problems/design-hashmap/description/
#
# algorithms
# Easy (54.03%)
# Likes:    350
# Dislikes: 59
# Total Accepted:    39.5K
# Total Submissions: 69.7K
# Testcase Example:  '["MyHashMap","put","put","get","get","put","get", "remove", "get"]\n[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]'
#
# Design a HashMap without using any built-in hash table libraries.
#
# To be specific, your design should include these functions:
#
#
# put(key, value) : Insert a (key, value) pair into the HashMap. If the value
# already exists in the HashMap, update the value.
# get(key): Returns the value to which the specified key is mapped, or -1 if
# this map contains no mapping for the key.
# remove(key) : Remove the mapping for the value key if this map contains the
# mapping for the key.
#
#
#
# Example:
#
#
# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);
# hashMap.put(2, 2);
# hashMap.get(1);            // returns 1
# hashMap.get(3);            // returns -1 (not found)
# hashMap.put(2, 1);          // update the existing value
# hashMap.get(2);            // returns 1
# hashMap.remove(2);          // remove the mapping for 2
# hashMap.get(2);            // returns -1 (not found)
#
#
#
# Note:
#
#
# All keys and values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashMap library.
#
#
#
# use the build-in HashMap can beats 86%
# class MyHashMap(object):
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.items = {}

#     def put(self, key, value):
#         """
#         value will always be non-negative.
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         self.items[key] = value

#     def get(self, key):
#         """
#         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
#         :type key: int
#         :rtype: int
#         """
#         return self.items.get(key, -1)

#     def remove(self, key):
#         """
#         Removes the mapping of the specified value key if this map contains a mapping for the key
#         :type key: int
#         :rtype: None
#         """
#         try:
#             self.items.pop(key)
#         except:
#             pass


# my solution, 70%
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1024
        self.items = [None] * self.m

    def hash(self, key):
        return key % self.m

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """

        old = self.items[self.hash(key)]
        if old is None:
            self.items[self.hash(key)] = Node(key, value)
            return
        while old is not None:
            if old.key == key:
                old.val = value
                return
            if old.next is None:
                break
            old = old.next
        old.next = Node(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        node = self.items[self.hash(key)]
        while node is not None:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        node = self.items[self.hash(key)]
        while node is not None:
            if node.key == key:
                node.val = None
                node.key = None
                return
            node = node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

