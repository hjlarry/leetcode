#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (34.21%)
# Likes:    1902
# Dislikes: 138
# Total Accepted:    408.1K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, remove the n-th node from the end of list and return its
# head.
#
# Example:
#
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes
# 1->2->3->5.
#
#
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    # A solution use fast and slow pointer, 64%
    # def removeNthFromEnd(self, head, n):
    #     """
    #     :type head: ListNode
    #     :type n: int
    #     :rtype: ListNode
    #     """
    #     cur = quick = head
    #     for _ in range(n):
    #         quick = quick.next
    #     if not quick:
    #         return head.next
    #     while quick.next is not None:
    #         quick=quick.next
    #         cur = cur.next
    #     cur.next = cur.next.next
    #     return head

    # 一个讨巧方案，并没有移动节点，而是移动节点的值，93%
    # def removeNthFromEnd(self, head, n):
    #     def index(node):
    #         if not node:
    #             return 0
    #         i = index(node.next) + 1
    #         if i>n:
    #             node.next.val = node.val
    #         return i
    #     index(head)
    #     return head.next

    # a top voted solution, 98%
    def removeNthFromEnd(self, head, n):
        self.next, nodelist = head, [self]
        while head.next:
            if len(nodelist) == n:
                nodelist.pop(0)
            nodelist.append(head)
            head = head.next
        nodelist[0].next = nodelist[0].next.next
        return self.next
