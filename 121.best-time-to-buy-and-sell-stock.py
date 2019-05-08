#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
class Solution:
    # my solution, beats 99.32 %
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        result = 0
        small = prices[0]
        i = 1
        while i < len(prices):
            if prices[i] < small:
                small = prices[i]
            elif prices[i] - small > result:
                result = prices[i] - small
            i += 1
        return result
