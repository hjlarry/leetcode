#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#
class Solution(object):

    # a voted solution, 99.13%
    # 这个方法效率很高  但不易理解
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 1
        start = 0
        for i in range(len(s)):
            if (
                i - maxLen >= 1
                and s[i - maxLen - 1 : i + 1] == s[i - maxLen - 1 : i + 1][::-1]
            ):
                start = i - maxLen - 1
                maxLen += 2
                continue
            if i - maxLen >= 0 and s[i - maxLen : i + 1] == s[i - maxLen : i + 1][::-1]:
                start = i - maxLen
                maxLen += 1
        return s[start : start + maxLen]

