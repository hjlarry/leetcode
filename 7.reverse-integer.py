#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.10%)
# Total Accepted:    606.1K
# Total Submissions: 2.4M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
#
# Input: 123
# Output: 321
#
#
# Example 2:
#
#
# Input: -123
# Output: -321
#
#
# Example 3:
#
#
# Input: 120
# Output: 21
#
#
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 0 when the reversed integer
# overflows.
#
#
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            result = int("".join(reversed(str(x))))
            if result < 2147483648:
                return result
        else:
            result = 0 - int("".join(reversed(str(x)[1:])))
            if result > -2147483649:
                return result
        return 0


print(Solution().reverse(1534236469))
