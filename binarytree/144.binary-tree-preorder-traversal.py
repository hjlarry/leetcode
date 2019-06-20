#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # my solution, 95%
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     result = []
    #     def helper(node, res):
    #         if node:
    #             res.append(node.val)
    #             helper(node.left, res)
    #             helper(node.right, res)
    #     helper(root, result)
    #     return result

    # top voted solution, use stack, 83%
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
