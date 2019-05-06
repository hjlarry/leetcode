#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
class Solution:
    # top voted solution
    def generate(self, numRows: int):
        results = [[1] * i for i in range(1, numRows + 1)]
        for i in range(numRows):
            for j in range(1, i):
                results[i][j] = results[i - 1][j - 1] + results[i - 1][j]
        return results


# Solution().generate(5)
