#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (45.52%)
# Total Accepted:    219.4K
# Total Submissions: 473.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its bottom-up level order traversal as:
#
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    #  my solution, only runtime beats 18.5 % of python3 submissions
    # def helper(self, node, depth):
    #     if node is not None:
    #         self.result[depth].append(node.val)
    #         self.helper(node.left, depth + 1)
    #         self.helper(node.right, depth + 1)

    # def levelOrderBottom(self, root):
    #     self.result = collections.defaultdict(list)
    #     self.helper(root, 1)
    #     result = []
    #     for _, item in sorted(self.result.items(), reverse=True):
    #         result.append(item)
    #     return result
    def helper(self, node, level, res):
        if node:
            if len(res) < level + 1:
                res.insert(0, [])
            res[-(level + 1)].append(node.val)
            self.helper(node.left, level + 1, res)
            self.helper(node.right, level + 1, res)

    def levelOrderBottom(self, root):
        res = []
        self.helper(root, 0, res)
        return res
