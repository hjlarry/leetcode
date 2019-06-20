#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
class Solution:
    # top voted solution
    def getRow(self, rowIndex: int) -> List[int]:
        results = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                results[i - j] += results[i - j - 1]
        return results
