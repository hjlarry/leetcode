#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input array is sorted
#
class Solution(object):
    # same as question 1 ?
    # 63.28% this solution
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = {}
        for index, value in enumerate(numbers, start=1):
            n = target - value
            if n in temp:
                return [temp[n], index]
            temp[value] = index
