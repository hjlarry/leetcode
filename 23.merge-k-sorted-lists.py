#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from functools import reduce


class Solution(object):
    # my solution, only beats 7.77%
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        def merge_two_linklist(c1, c2):
            current = first = ListNode(0)
            while c1 is not None and c2 is not None:
                if c1.val <= c2.val:
                    current.next = c1
                    c1 = c1.next
                else:
                    current.next = c2
                    c2 = c2.next
                current = current.next
            if c1:
                current.next = c1
            else:
                current.next = c2
            return first.next

        return reduce(merge_two_linklist, lists)

