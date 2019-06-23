#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode(object):
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

