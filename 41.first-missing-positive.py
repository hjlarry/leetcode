#
# @lc app=leetcode id=41 lang=python
#
# [41] First Missing Positive
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
