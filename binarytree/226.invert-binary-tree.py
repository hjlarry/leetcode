#
# @lc app=leetcode id=226 lang=python
#
# [226] Invert Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # my solution , 66%
    # def invertTree(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: TreeNode
    #     """
    #     if root is not None:
    #         root.left, root.right = root.right, root.left
    #         self.invertTree(root.left)
    #         self.invertTree(root.right)
    #     return root

    # top voted one line solution, 98%
    # def invertTree(self, root):
    #     if root:
    #         root.left, root.right = (
    #             self.invertTree(root.right),
    #             self.invertTree(root.left),
    #         )
    #         return root

    #  not use recusive solution, 92%
    def invertTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root
