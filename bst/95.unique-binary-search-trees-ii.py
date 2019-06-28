#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (35.56%)
# Likes:    1274
# Dislikes: 115
# Total Accepted:    141.8K
# Total Submissions: 393.6K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
#
# Example:
#
#
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # a top voted solution, 41%
    def trees(self, first, last):
        trees = []
        for root in range(first, last + 1):
            for left in self.trees(first, root - 1):
                for right in self.trees(root + 1, last):
                    node = TreeNode(root)
                    node.left = left
                    node.right = right
                    trees.append(node)
        return trees or [None]

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.trees(1, n)

    # a top voted solution, 72%
    # def generateTrees(self, n):
    #     if n == 0:
    #         return []
    #     def node(val, left, right):
    #         node = TreeNode(val)
    #         node.left = left
    #         node.right = right
    #         return node
    #     def trees(first, last):
    #         return [node(root, left, right)
    #                 for root in range(first, last+1)
    #                 for left in trees(first, root-1)
    #                 for right in trees(root+1, last)] or [None]
    #     return trees(1, n)
