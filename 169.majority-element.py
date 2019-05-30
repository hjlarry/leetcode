#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#


class Solution(object):
    # my solution 45%
    # from collections import Counter

    # def majorityElement(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     items = Counter(nums)
    #     return items.most_common(1)[0][0]
    # top voted solution, 67%
    def majorityElement(self, nums):
        return sorted(nums)[len(nums) // 2]


# print(Solution().majorityElement([3, 2, 3]))
