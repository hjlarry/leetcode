#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # my solution use layer travel, 78.6%
    # def rightSideView(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     current_nodes = [root]
    #     next_nodes = []
    #     res = []
    #     while current_nodes or next_nodes:
    #         for node in current_nodes:
    #             if node.left:
    #                 next_nodes.append(node.left)
    #             if node.right:
    #                 next_nodes.append(node.right)
    #         res.append(current_nodes[-1].val)
    #         current_nodes = next_nodes
    #         next_nodes = []
    #     return res

    # top voted solution , 78%, O(n)
    # def rightSideView(self, root: TreeNode):
    #     res = []

    #     def collect(node, depth):
    #         if node:
    #             if depth == len(res):
    #                 res.append(node.val)
    #             collect(node.right, depth + 1)
    #             collect(node.left, depth + 1)

    #     collect(root, 0)
    #     return res

    # top voted solution , 91%, 但对于非常不平衡的树，可能是O(n^2)
    def rightSideView(self, root: TreeNode):
        if not root:
            return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return [root.val] + right + left[len(right) :]
