#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (28.79%)
# Likes:    1657
# Dislikes: 570
# Total Accepted:    214K
# Total Submissions: 739.9K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
#
# Input: [1,2,0]
# Output: 3
#
#
# Example 2:
#
#
# Input: [3,4,-1,1]
# Output: 2
#
#
# Example 3:
#
#
# Input: [7,8,9,11,12]
# Output: 1
#
#
# Note:
#
# Your algorithm should run in O(n) time and uses constant extra space.
#
#
class Solution(object):
    # my solution beats 99%
    # 但实际上是一个O(n^2)的算法，因为找一个数是否在list中复杂度是O(n)的
    # def firstMissingPositive(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     for i in range(1, len(nums) + 2):
    #         if i not in nums:
    #             return i

    # 先排序再匹配， 69%， O(nlogn)
    # def firstMissingPositive(self, nums):
    #     nums.sort()
    #     res = 1
    #     for num in nums:
    #         if num == res:
    #             res += 1
    #     return res

    # top voted, 69%, O(n)
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while 0 <= nums[i] - 1 < len(nums) and nums[nums[i] - 1] != nums[i]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
