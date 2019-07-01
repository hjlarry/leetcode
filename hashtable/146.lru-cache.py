#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Hard (25.25%)
# Likes:    2943
# Dislikes: 104
# Total Accepted:    303.2K
# Total Submissions: 1.2M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# The cache is initialized with a positive capacity.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
# 
# 
#


# My solution,双向链表加哈希表 84%
# class Node:
#     def __init__(self, key=None, value=None, prev=None, next=None):
#         self.key, self.value, self.prev, self.next = key, value, prev, next


# class LRUCache(object):
#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.capacity = capacity
#         self.head = Node()  # 哨兵节点
#         self.tail = Node(prev=self.head)
#         self.head.next = self.tail
#         self.keys = {}

#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if key not in self.keys:
#             return -1
#         # 更新该节点的前后节点
#         current_node = self.keys[key]
#         current_node.prev.next = current_node.next
#         current_node.next.prev = current_node.prev
#         # 将该节点插入首节点
#         self.head.next.prev = current_node
#         current_node.next = self.head.next
#         self.head.next = current_node
#         current_node.prev = self.head

#         return current_node.value

#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         if key not in self.keys:
#             # 新key，插入首节点
#             new_node = Node(key, value, prev=self.head)
#             self.keys[key] = new_node
#             temp = self.head.next
#             self.head.next = new_node
#             new_node.next = temp
#             temp.prev = new_node
#             if len(self.keys) > self.capacity:
#                 # 大于容量时删除尾节点
#                 need_del = self.tail.prev
#                 need_del.prev.next = self.tail
#                 self.tail.prev = need_del.prev
#                 del self.keys[need_del.key]
#         else:
#             # 否则更新该节点的前后节点
#             current_node = self.keys[key]
#             current_node.value = value
#             current_node.prev.next = current_node.next
#             current_node.next.prev = current_node.prev
#             # 将该节点插入首节点
#             self.head.next.prev = current_node
#             current_node.next = self.head.next
#             self.head.next = current_node
#             current_node.prev = self.head


import collections

# Top voted solution with orderdict, 46%
class LRUCache(object):
    def __init__(self, capacity):
        self.remain = capacity
        self.items = collections.OrderedDict()

    def get(self, key):
        if key not in self.items:
            return -1
        # 一个更合理的实现，但leetcode不支持move_to_end方法，无法通过验证
        # value = self.items[key]
        # self.items.move_to_end(key)

        value = self.items.pop(key)
        self.items[key] = value
        return value

    def put(self, key, value):
        if key in self.items:
            self.items.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.items.popitem(last=False)
        self.items[key] = value
