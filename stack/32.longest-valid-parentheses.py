#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
class Solution:
    # top voted solution, 97%
    def longestValidParentheses(self, s: str) -> int:
        stack = [0] # 用最后一位存储最长的数值
        longest = 0

        for ch in s:
            if ch == '(':
                stack.append(0)
            elif ch == ')':
                if len(stack) >1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]
        return longest


