#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
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
