#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # top voted solution, 82%
    # def constructFromPrePost(self, pre, post):
    #     if not pre:
    #         return None
    #     root = TreeNode(pre[0])
    #     if len(pre) == 1:
    #         return root
    #     l = post.index(pre[1])+1
    #     root.left = self.constructFromPrePost(pre[1:l+1], post[:l])
    #     root.right = self.constructFromPrePost(pre[l+1:], post[l:-1])
    #     return root

    # another solution use stack, 100%
    def constructFromPrePost(self, pre, post):
        stack = [TreeNode(pre[0])]
        j = 0
        for v in pre[1:]:
            node = TreeNode(v)
            while stack[-1].val == post[j]:
                stack.pop()
                j+=1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
