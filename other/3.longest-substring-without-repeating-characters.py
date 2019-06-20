#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#
class Solution(object):
    # 滑动窗口法， 85.7%
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        a = set()
        current_len = 0
        max_len = 0
        for i in range(len(s)):
            current_len += 1
            while s[i] in a:
                a.remove(s[left])
                left += 1
                current_len -= 1
            if current_len > max_len:
                max_len = current_len
            a.add(s[i])
        return max_len
