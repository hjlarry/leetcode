#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
class Solution:
    # my solution, only 5.73%
    def singleNumber(self, nums) -> int:
        current = nums.pop()
        while True:
            if current in nums:
                nums.remove(current)
                current = nums.pop()
            else:
                break
        return current

