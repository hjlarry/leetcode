#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
class Solution:
    # my solution, only 5.73%
    # def singleNumber(self, nums) -> int:
    #     current = nums.pop()
    #     while True:
    #         if current in nums:
    #             nums.remove(current)
    #             current = nums.pop()
    #         else:
    #             break
    #     return current
    # top voted solution , 45.21%
    # def singleNumber(self, nums) -> int:
    #     res = 0
    #     for num in nums:
    #         res ^= num
    #     return res
    # top voted solution , 94.86%
    def singleNumber(self, nums) -> int:
        return 2 * sum(set(nums)) - sum(nums)
