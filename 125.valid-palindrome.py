#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # a slow solution, 13.8%
        test = []
        for a in s:
            if a in string.ascii_letters + string.digits:
                test.append(a.lower())
        test1 = list(reversed(test))
        if test1 == test:
            return True
        return False


# print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
