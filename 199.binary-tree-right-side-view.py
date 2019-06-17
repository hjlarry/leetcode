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
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        current_nodes = [root]
        next_nodes = []
        res = []
        while current_nodes or next_nodes:
            for node in current_nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            res.append(current_nodes[-1].val)
            current_nodes = next_nodes
            next_nodes = []
        return res

