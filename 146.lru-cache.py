#
# @lc app=leetcode id=146 lang=python
#
# [146] LRU Cache
#


# My solution, 84%
class Node:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key, self.value, self.prev, self.next = key, value, prev, next


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = Node()  # 哨兵节点
        self.tail = Node(prev=self.head)
        self.head.next = self.tail
        self.keys = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keys:
            return -1
        # 更新该节点的前后节点
        current_node = self.keys[key]
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        # 将该节点插入首节点
        self.head.next.prev = current_node
        current_node.next = self.head.next
        self.head.next = current_node
        current_node.prev = self.head

        return current_node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.keys:
            # 新key，插入首节点
            new_node = Node(key, value, prev=self.head)
            self.keys[key] = new_node
            temp = self.head.next
            self.head.next = new_node
            new_node.next = temp
            temp.prev = new_node
            if len(self.keys) > self.capacity:
                # 大于容量时删除尾节点
                need_del = self.tail.prev
                need_del.prev.next = self.tail
                self.tail.prev = need_del.prev
                del self.keys[need_del.key]
        else:
            # 否则更新该节点的前后节点
            current_node = self.keys[key]
            current_node.value = value
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            # 将该节点插入首节点
            self.head.next.prev = current_node
            current_node.next = self.head.next
            self.head.next = current_node
            current_node.prev = self.head


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

