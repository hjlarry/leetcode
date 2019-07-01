#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (34.27%)
# Likes:    2475
# Dislikes: 162
# Total Accepted:    393.1K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
#
# Example:
#
#
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    # my solution, only beats 7.77%
    # def mergeKLists(self, lists):
    #     """
    #     :type lists: List[ListNode]
    #     :rtype: ListNode
    #     """
    #     if not lists:
    #         return None

    #     def merge_two_linklist(c1, c2):
    #         current = first = ListNode(0)
    #         while c1 is not None and c2 is not None:
    #             if c1.val <= c2.val:
    #                 current.next = c1
    #                 c1 = c1.next
    #             else:
    #                 current.next = c2
    #                 c2 = c2.next
    #             current = current.next
    #         if c1:
    #             current.next = c1
    #         else:
    #             current.next = c2
    #         return first.next

    #     return reduce(merge_two_linklist, lists)

    # 一个不正确的方案，但不好debug
    # def mergeKLists(self, lists):
    #     current = first = ListNode(0)
    #     while len(lists) > 0:
    #         the_min = min(lists, key=lambda item: item.val)
    #         temp = the_min
    #         if the_min.next is not None:
    #             the_min = the_min.next
    #         else:
    #             lists.pop(the_min)
    #         current.next = temp
    #         current = current.next
    #     return first.next

    # 和方案一类似，但使用递归解决， 63%
    # def merge_two_linklist(self, c1, c2):
    #     current = first = ListNode(0)
    #     while c1 is not None and c2 is not None:
    #         if c1.val <= c2.val:
    #             current.next = c1
    #             c1 = c1.next
    #         else:
    #             current.next = c2
    #             c2 = c2.next
    #         current = current.next
    #     current.next = c1 or c2
    #     return first.next

    # def mergeKLists(self, lists):
    #     if not lists:
    #         return None
    #     if len(lists) == 1:
    #         return lists[0]
    #     mid = len(lists) // 2
    #     left = self.mergeKLists(lists[:mid])
    #     right = self.mergeKLists(lists[mid:])
    #     return self.merge_two_linklist(left, right)

    # top voted solution，使用堆排序， 83%
    import heapq

    def mergeKLists(self, lists):
        current = first = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        heapq.heapify(h)
        while h:
            v, n = h[0]
            if n.next is None:
                heapq.heappop(h)
            else:
                heapq.heapreplace(h, (n.next.val, n.next))
            current.next = n
            current = current.next
        return first.next
