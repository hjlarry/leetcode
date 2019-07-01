#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (23.93%)
# Likes:    3801
# Dislikes: 425
# Total Accepted:    554.8K
# Total Submissions: 2.3M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#


class Solution(object):

    # top voted solution ， 95%
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:  # 排序后只遍历小于0的部分
                break
            if i > 0 and nums[i] == nums[i - 1]:  # 相同的数字，只处理一次
                continue

            l, r = i + 1, len(nums) - 1  # 设置左右两个flag
            while l < r:
                s = nums[i] + nums[l] + nums[r]  # 根据s的值移动flag
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:  # 相同的flag可以忽略
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1  # 找出当前i所有可能的情况
                    r -= 1
        return res
