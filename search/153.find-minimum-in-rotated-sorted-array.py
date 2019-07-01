#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (42.91%)
# Likes:    989
# Dislikes: 161
# Total Accepted:    288.3K
# Total Submissions: 669.9K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Example 1:
#
#
# Input: [3,4,5,1,2]
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,5,6,7,0,1,2]
# Output: 0
#
#
#
class Solution:
    # my solution but refer to others, 94%
    # def findMin(self, nums: List[int]) -> int:
    #     low, high = 0, len(nums) - 1
    #     while low < high:
    #         mid = low + (high - low) // 2
    #         if nums[mid] > nums[high]:
    #             low = mid + 1
    #         else:
    #             high = mid
    #     return nums[low]

    # 80%, top voted solution :)
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
