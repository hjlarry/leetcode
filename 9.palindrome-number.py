#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (41.83%)
# Total Accepted:    508.5K
# Total Submissions: 1.2M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
#
# Example 1:
#
#
# Input: 121
# Output: true
#
#
# Example 2:
#
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
#
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
# Follow up:
#
# Coud you solve it without converting the integer to a string?
#
#
class Solution:
    # 前两个方案都是通过比较字符串，方案三是翻转数字
    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0:
    #         return False
    #     string = str(x)
    #     length = len(string)
    #     mid = length // 2
    #     if length % 2 == 0:
    #         for i in range(0, mid):
    #             if string[mid + i] != string[mid - 1 - i]:
    #                 return False
    #     else:
    #         for i in range(1, mid + 1):
    #             if string[mid + i] != string[mid - i]:
    #                 return False
    #     return True
    # def isPalindrome(self, x: int) -> bool:
    #     return str(x) == str(x)[::-1]
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        p, res = x, 0
        while p:
            res = res * 10 + p % 10
            p = p // 10
        return res == x


# print(Solution().isPalindrome(12123))
# print(Solution().isPalindrome(1331))
