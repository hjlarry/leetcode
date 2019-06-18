#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#
class Solution(object):

    # a voted solution, 99.13%
    # 这个方法效率很高  但不易理解
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     maxLen = 1
    #     start = 0
    #     for i in range(len(s)):
    #         if (
    #             i - maxLen >= 1
    #             and s[i - maxLen - 1 : i + 1] == s[i - maxLen - 1 : i + 1][::-1]
    #         ):
    #             start = i - maxLen - 1
    #             maxLen += 2
    #             continue
    #         if i - maxLen >= 0 and s[i - maxLen : i + 1] == s[i - maxLen : i + 1][::-1]:
    #             start = i - maxLen
    #             maxLen += 1
    #     return s[start : start + maxLen]

    # top voted solution, 74.35%
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]

