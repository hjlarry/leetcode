#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (43.11%)
# Total Accepted:    495.3K
# Total Submissions: 1.1M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# Example:
#
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
#
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
class Solution:
    # def maxSubArray(self, nums) -> int:
    #     res = nums[0]
    #     sum_ = 0
    #     for num in nums:
    #         if sum_ > 0:
    #             sum_ += num
    #         else:
    #             sum_ = num
    #         res = max([res, sum_])
    #     return res
    # nums[i-1]并不是数组前一项的意思，而是到前一项为止的最大子序和，和0比较是因为只要大于0，就可以相加构造最大子序和
    # 如果小于0则相加为0，nums[i]=nums[i]，相当于最大子序和又重新计算。其实是一边遍历一边计算最大序和
    def maxSubArray(self, nums) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0)
        return max(nums)


# print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
