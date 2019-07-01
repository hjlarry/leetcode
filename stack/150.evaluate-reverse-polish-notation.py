#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (32.07%)
# Likes:    517
# Dislikes: 348
# Total Accepted:    163.7K
# Total Submissions: 506.5K
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# Valid operators are +, -, *, /. Each operand may be an integer or another
# expression.
# 
# Note:
# 
# 
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would
# always evaluate to a result and there won't be any divide by zero
# operation.
# 
# 
# Example 1:
# 
# 
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# 
# 
# Example 2:
# 
# 
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# 
# 
# Example 3:
# 
# 
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation: 
# ⁠ ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
# 
#
import operator


class Solution(object):
    # 这个解决方案应该是正确的，只是leetcode不支持eval表达式，而且其 6 // -132结果为-1，6 // 132结果为0，造成验证不通过
    # tmp = {
    #     "+": operator.add,
    #     "-": operator.sub,
    #     "*": operator.mul,
    #     "/": operator.floordiv,
    # }

    # def evalRPN(self, tokens):
    #     """
    #     :type tokens: List[str]
    #     :rtype: int
    #     """
    #     stack = []
    #     for t in tokens:
    #         if t in "+-*/":
    #             a, b = int(stack.pop()), int(stack.pop())
    #             print(a, b)
    #             res = tmp.get(t)(b, a)
    #             print(res)
    #             stack.append(res)
    #         else:
    #             stack.append(t)
    #     return stack.pop()

    # top voted solution, 62%
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t in "+-*/":
                a, b = int(stack.pop()), int(stack.pop())
                if t == "+":
                    stack.append(b + a)
                elif t == "-":
                    stack.append(b - a)
                elif t == "*":
                    stack.append(b * a)
                else:
                    # 解决6//-132在python中结果为-1，而在leetcode中结果为0
                    if a * b < 0 and b % a != 0:
                        stack.append(b // a + 1)
                    else:
                        stack.append(b // a)
            else:
                stack.append(t)
        return stack.pop()


# Solution().evalRPN(
#     ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# )
