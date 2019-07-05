#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (44.47%)
# Likes:    1197
# Dislikes: 105
# Total Accepted:    325.9K
# Total Submissions: 721.7K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
#
#
#
# Example:
#
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # top voted solution, 99%
    def swapPairs(self, head: ListNode) -> ListNode:
        dummpy = current = ListNode(None)
        dummpy.next = head
        while current.next and current.next.next:
            a = current.next
            b = a.next
            current.next, a.next, b.next = b, b.next, a
            current = a

        return dummpy.next
