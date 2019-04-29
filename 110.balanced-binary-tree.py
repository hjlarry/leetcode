#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 递归求出树高，再递归求出是否平衡二叉树，效率很低
    def treeHeight(self, root):
        if root is None:
            return 0
        root_l = self.treeHeight(root.left)
        root_r = self.treeHeight(root.right)
        if root_l > root_r:
            return root_l + 1
        return root_r + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left_height = self.treeHeight(root.left)
        right_height = self.treeHeight(root.right)
        gap = right_height - left_height
        if gap > 1 or gap < -1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

