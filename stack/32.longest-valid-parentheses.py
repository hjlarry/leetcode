#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (25.40%)
# Likes:    1891
# Dislikes: 90
# Total Accepted:    193.7K
# Total Submissions: 756.1K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
#
#
# Example 2:
#
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
#
#
#
class Solution:
    # top voted solution, 97%
    def longestValidParentheses(self, s: str) -> int:
        stack = [0]  # 用最后一位存储最长的数值
        longest = 0

        for ch in s:
            if ch == "(":
                stack.append(0)
            elif ch == ")":
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]
        return longest
