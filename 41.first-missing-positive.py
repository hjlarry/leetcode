#
# @lc app=leetcode id=41 lang=python
#
# [41] First Missing Positive
#
class Solution(object):
    # my solution beats 99%
    # 但实际上是一个O(n^2)的算法，因为找一个数是否在list中复杂度是O(n)的
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums) + 2):
            if i not in nums:
                return i

