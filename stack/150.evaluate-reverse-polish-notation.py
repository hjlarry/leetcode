#
# @lc app=leetcode id=150 lang=python
#
# [150] Evaluate Reverse Polish Notation
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
