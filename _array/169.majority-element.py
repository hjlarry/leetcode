#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (52.47%)
# Likes:    1638
# Dislikes: 142
# Total Accepted:    383.1K
# Total Submissions: 727.7K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
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
