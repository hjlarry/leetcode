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
    # my solution, 73.69%
    # def hasCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     current = head
    #     storage = set()
    #     while current is not None:
    #         if current in storage:
    #             return True
    #         storage.add(current)
    #         current = current.next
    #     return False
    # top voted solution 98.98 %
    # 采用快慢两个指针，达到空间复杂度O(1)，让两个指针的移动速度不同，若为环，则快的一定会追上慢的
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow is not fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

