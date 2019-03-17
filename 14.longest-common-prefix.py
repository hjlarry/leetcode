#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (32.95%)
# Total Accepted:    421.5K
# Total Submissions: 1.3M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#
#
class Solution:
    # def longestCommonPrefix(self, strs) -> str:
    #     result = ""
    #     index = 0
    #     if not strs:
    #         return result
    #     while index < len(strs[0]):
    #         current = strs[0][index]
    #         all_equal = True
    #         for item in strs:
    #             if index >= len(item) or item[index] != current:
    #                 all_equal = False
    #                 break
    #         if all_equal:
    #             result += current
    #             index += 1
    #         else:
    #             break

    # return result
    def longestCommonPrefix(self, strs) -> str:
        result = ""
        items = zip(*strs)
        for item in items:
            if len(set(item)) > 1:
                break
            result += item[0]
        return result

