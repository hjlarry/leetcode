#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
class Solution:
    # my solution but refer to others, 94%
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low < high :
            mid = low + (high-low) // 2
            if nums[mid] >nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

