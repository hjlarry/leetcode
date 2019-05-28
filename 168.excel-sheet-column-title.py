#
# @lc app=leetcode id=168 lang=python
#
# [168] Excel Sheet Column Title
#


class Solution(object):
    # a solution beats 94%
    def convertToTitle(self, n):
        ab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        pre = self.convertToTitle((n - 1) // 26) if (n - 1) // 26 != 0 else ""
        return pre + ab[(n - 1) % 26]
