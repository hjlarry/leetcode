#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (49.65%)
# Total Accepted:    365.7K
# Total Submissions: 734.9K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given two binary trees, write a function to check if they are the same or
# not.
#
# Two binary trees are considered the same if they are structurally identical
# and the nodes have the same value.
#
# Example 1:
#
#
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
#
# ⁠       [1,2,3],   [1,2,3]
#
# Output: true
#
#
# Example 2:
#
#
# Input:     1         1
# ⁠         /           \
# ⁠        2             2
#
# ⁠       [1,2],     [1,null,2]
#
# Output: false
#
#
# Example 3:
#
#
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
#
# ⁠       [1,2,1],   [1,1,2]
#
# Output: false
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 这个思路尝试先序遍历两个二叉树，得到两个列表进行比较，但问题是当左子树为空时，并没有在列表中append(null)
    # def iter_tree(self, subtree, result):
    #     if subtree is not None:
    #         result.append(subtree.val)
    #         self.iter_tree(subtree.left, result)
    #         self.iter_tree(subtree.right, result)

    #     return result

    # def isSameTree(self, p, q) -> bool:
    #     result_p = self.iter_tree(p, [])
    #     result_q = self.iter_tree(q, [])
    #     return result_p == result_q
    # def isSameTree(self, p, q) -> bool:
    #     if p and q:
    #         return (
    #             p.val == q.val
    #             and self.isSameTree(p.left, q.left)
    #             and self.isSameTree(p.right, q.right)
    #         )
    #     return p is q

    def isSameTree(self, p, q) -> bool:
        if p == q == None:
            return True
        if None in [p, q] or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

