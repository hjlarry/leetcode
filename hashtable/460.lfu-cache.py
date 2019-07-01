#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#
# https://leetcode.com/problems/lfu-cache/description/
#
# algorithms
# Hard (28.73%)
# Likes:    667
# Dislikes: 75
# Total Accepted:    40.3K
# Total Submissions: 139.3K
# Testcase Example:  '["LFUCache","put","put","get","put","get","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Frequently Used (LFU) cache.
# It should support the following operations: get and put.
#
#
#
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reaches its capacity, it should invalidate the least
# frequently used item before inserting a new item. For the purpose of this
# problem, when there is a tie (i.e., two or more keys that have the same
# frequency), the least recently used key would be evicted.
#
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LFUCache cache = new LFUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
#
#
#
# LFU算法，缓存满时，替换掉一个最少使用的key
# 参考 https://github.com/PegasusWang/python_data_structures_and_algorithms/blob/master/docs/15_%E5%A0%86%E4%B8%8E%E5%A0%86%E6%8E%92%E5%BA%8F/lfu.py?1560490372553
# 53%
import collections


class Node:
    def __init__(self, key, value, count=0):
        self.key, self.value, self.count = key, value, count


class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}  # key:key, value:Node()
        # key: 使用次数, value: {key: key, value:Node()}
        self.count_to_node = collections.defaultdict(collections.OrderedDict)
        self.min_count = 0  # 当前缓存里最少使用的次数是几

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        del self.count_to_node[node.count][key]

        node.count += 1
        self.count_to_node[node.count][key] = node

        if not self.count_to_node[self.min_count]:
            self.min_count += 1

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache[key].value = value
            self.get(key)
            return
        if self.capacity == 0:
            return
        if len(self.cache) >= self.capacity:
            need_pop_key, need_pop_node = self.count_to_node[self.min_count].popitem(
                last=False
            )
            del self.cache[need_pop_key]
        self.cache[key] = self.count_to_node[1][key] = Node(key, value, 1)
        self.min_count = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
