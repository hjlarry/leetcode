#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # top voted solution , 84%
        # 若一个节点移动的快，另一个移动的慢，则移动快的a结束时指向headB，最终就会追上b
        current_a = headA
        current_b = headB
        while current_a is not current_b:
            current_a = headB if current_a is None else current_a.next
            current_b = headA if current_b is None else current_b.next
        return current_a

