#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (25.67%)
# Likes:    1955
# Dislikes: 294
# Total Accepted:    411.3K
# Total Submissions: 1.6M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
#
# Example 1:
#
#
# ⁠   2
# ⁠  / \
# ⁠ 1   3
#
# Input: [2,1,3]
# Output: true
#
#
# Example 2:
#
#
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # a voted recusive solution, 98%
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     def valid(node, low, high):
    #         if node is None:
    #             return True
    #         if low is not None and node.val <= low:
    #             return False
    #         if high is not None and node.val >= high:
    #             return False
    #         return valid(node.left, low, node.val) and valid(node.right, node.val, high)

    #     return valid(root, None, None)

    # top voted, 用中序遍历的方法，也是98%
    def isValidBST(self, root):
        def inorder(node, output):
            if node is None:
                return
            inorder(node.left, output)
            output.append(node.val)
            inorder(node.right, output)

        output = []
        inorder(root, output)
        for i in range(1, len(output)):
            if output[i] <= output[i - 1]:
                return False
        return True
