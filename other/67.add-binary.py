#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (38.40%)
# Total Accepted:    289.4K
# Total Submissions: 751.3K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
class Solution:
    # def addBinary(self, a: str, b: str) -> str:
    #     return str(bin(int(a, 2) + int(b, 2)))[2:]
    def addBinary(self, a: str, b: str) -> str:
        return f"{int(a,2)+int(b,2):b}"


# print(Solution().addBinary(a="1010", b="1011"))
