#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # my solution 81.46%
    def hasPathSum(self, root, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None and sum == root.val:
            return True
        left = self.hasPathSum(root.left, sum - root.val)
        right = self.hasPathSum(root.right, sum - root.val)
        if left or right:
            return True
        return False

