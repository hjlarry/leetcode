#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (40.59%)
# Total Accepted:    377.3K
# Total Submissions: 929.4K
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
#
# Input: [1,3,5,6], 5
# Output: 2
#
#
# Example 2:
#
#
# Input: [1,3,5,6], 2
# Output: 1
#
#
# Example 3:
#
#
# Input: [1,3,5,6], 7
# Output: 4
#
#
# Example 4:
#
#
# Input: [1,3,5,6], 0
# Output: 0
#
#
#
class Solution:
    # 可能是因为测试用例的数据较小，遍历反而比二分查找效率更高
    #   ✔ 62/62 cases passed (52 ms)
    #   ✔ Your runtime beats 17.59 % of python3 submissions
    #   ✔ Your memory usage beats 5.11 % of python3 submissions (13.6 MB)
    # def searchInsert(self, nums, target) -> int:
    #     low = 0
    #     high = len(nums) - 1
    #     while low <= high:
    #         pos = low + (high - low) // 2
    #         if nums[pos] >= target:
    #             if pos == 0 or nums[pos - 1] < target:
    #                 return pos
    #             else:
    #                 high = pos - 1
    #         else:
    #             low = pos + 1
    #     return pos + 1
    #   ✔ 62/62 cases passed (36 ms)
    #   ✔ Your runtime beats 91.59 % of python3 submissions
    #   ✔ Your memory usage beats 5.11 % of python3 submissions (13.6 MB)
    def searchInsert(self, nums, target) -> int:
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)


# print(Solution().searchInsert([1, 3, 5, 6], 7))
