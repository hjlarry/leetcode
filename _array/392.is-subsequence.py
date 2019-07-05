#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#
# https://leetcode.com/problems/is-subsequence/description/
#
# algorithms
# Medium (46.65%)
# Likes:    571
# Dislikes: 130
# Total Accepted:    91K
# Total Submissions: 193.8K
# Testcase Example:  '"abc"\n"ahbgdc"'
#
#
# Given a string s and a string t, check if s is subsequence of t.
#
#
#
# You may assume that there is only lower case English letters in both s and t.
# t is potentially a very long (length ~= 500,000) string, and s is a short
# string (
#
#
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ace" is a
# subsequence of "abcde" while "aec" is not).
#
#
# Example 1:
# s = "abc", t = "ahbgdc"
#
#
# Return true.
#
#
# Example 2:
# s = "axc", t = "ahbgdc"
#
#
# Return false.
#
#
# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you
# want to check one by one to see if T has its subsequence. In this scenario,
# how would you change your code?
#
# Credits:Special thanks to @pbrother for adding this problem and creating all
# test cases.
#
class Solution:
    # my solution, only 23%
    # def isSubsequence(self, s: str, t: str) -> bool:
    #     a = b = 0
    #     while a < len(s) and b < len(t):
    #         if s[a] == t[b]:
    #             a += 1
    #         b += 1

    #     if a >= len(s):
    #         return True
    #     return False

    # top voted solution, 83% 代码注释见最下方
    # def isSubsequence(self, s: str, t: str) -> bool:
    #     t = iter(t)
    #     return all(i in t for i in s)

    # another top voted solution, 97%
    def isSubsequence(self, s: str, t: str) -> bool:
        last = -1
        for char in s:
            try:
                last = t.index(char, last + 1)
            except:
                return False
        return True


"""
def is_subsequence(a, b): 
    # 把 b 变为一个迭代器，这样每次调用for循环实际是调用next，会让它往前走
    b = iter(b)
    print(b)
    gen = (i for i in a) 
    print(gen)
    for i in gen:
        print(i)
    # (i in b) 等价于
    # while True:
    #    val = next(b)
    #    if val == i:
    #       yield True

    # 另一个例子:
    # b = (i for i in range(5))
    # print((2 in b))
    # print((4 in b))
    # print((3 in b))
    gen = ((i in b) for i in a) 
    print(gen)
    for i in gen:
        print(i)
    return all(((i in b) for i in a))
"""
