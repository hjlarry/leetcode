#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


class Solution:
    # a slow solution, 13.8%
    # def isPalindrome(self, s: str) -> bool:
    #     test = []
    #     for a in s:
    #         if a in string.ascii_letters + string.digits:
    #             test.append(a.lower())
    #     test1 = list(reversed(test))
    #     if test1 == test:
    #         return True
    #     return False

    # my better solution, 76.94 %
    # def isPalindrome(self, s: str) -> bool:
    #     test = [None]
    #     for a in s:
    #         if a.isalnum():
    #             test.append(a.lower())
    #     i = 1
    #     while i < len(test) // 2 + 1:
    #         if test[i] != test[-i]:
    #             return False
    #         i += 1
    #     return True

    # top voted solution, 46 %
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


# print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
