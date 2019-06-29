#
# @lc app=leetcode id=173 lang=python
#
# [173] Binary Search Tree Iterator
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator(object):
    # my solution use preorder iter, 58%
    # my solution use postorder iter, 74%
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.items = []
        self.iter_items(self.root)
        # self.items = self.items[::-1]

    def iter_items(self, root):
        if root is not None:
            self.iter_items(root.right)
            self.items.append(root.val)
            self.iter_items(root.left)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self.items.pop()

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.items) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
