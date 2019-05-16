#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # my solution, 73.69%
        current = head
        storage = set()
        while current is not None:
            if current in storage:
                return True
            storage.add(current)
            current = current.next
        return False

