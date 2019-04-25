#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # my solution
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = "", ""
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        while l2:
            s2 += str(l2.val)
            l2 = l2.next

        res = int(s1[::-1]) + int(s2[::-1])
        res = str(res)[::-1]
        i = 0
        first = cur = ListNode(int(res[i]))
        while i < len(res) - 1:
            i += 1
            next = ListNode(int(res[i]))
            cur.next = next
            cur = next

        return first

