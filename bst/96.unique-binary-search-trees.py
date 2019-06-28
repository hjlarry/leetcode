#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (46.05%)
# Likes:    1764
# Dislikes: 68
# Total Accepted:    204.1K
# Total Submissions: 438.3K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
#
# Example:
#
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#
import math


class Solution:
    # A top voted solution use DP, 90%
    # seen = {0:1, 1:1}
    # def numTrees(self, n: int) -> int:
    #     if n in self.seen:
    #         return self.seen.get(n)

    #     result = 0
    #     for i in range(1,n+1):
    #         left_trees = self.seen.get(i-1, self.numTrees(i-1))
    #         right_trees = self.seen.get(n-i, self.numTrees(n-i))
    #         result += left_trees * right_trees
    #     self.seen[i] = result
    #     return result

    # 使用数学方法，它也叫Catalan Number， (2n)!/((n+1)!*n!) ， 71%
    def numTrees(self, n: int) -> int:
        return int(math.factorial(2 * n) / (math.factorial(n) * math.factorial(n + 1)))
