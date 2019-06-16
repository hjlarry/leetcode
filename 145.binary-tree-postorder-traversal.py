#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # my solution use rescusive, 82%
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     result = []
    #     def helper(node, res):
    #         if node:
    #             helper(node.left, res)
    #             helper(node.right, res)
    #             res.append(node.val)
    #     helper(root, result)
    #     return result

    # my solution use stack, 99%
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return result[::-1]


