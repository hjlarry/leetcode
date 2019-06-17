#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
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

