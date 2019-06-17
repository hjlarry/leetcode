#
# @lc app=leetcode id=239 lang=python
#
# [239] Sliding Window Maximum
#
import collections


class Solution(object):

    # my solution, only 20%
    # def init(self, maxsize):
    #     self.items = [None] * maxsize
    #     self.maxsize = maxsize
    #     self.head = 0
    #     self.tail = 0

    # def enqueue(self, item):
    #     if self.head - self.tail >= self.maxsize:
    #         return False
    #     self.items[self.head % self.maxsize] = item
    #     self.head += 1
    #     return True

    # def dequeue(self):
    #     item = self.items[self.tail % self.maxsize]
    #     self.tail += 1
    #     return item

    # def maxSlidingWindow(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: List[int]
    #     """
    #     if not nums or len(nums) < k:
    #         return []
    #     result = []
    #     self.init(k)
    #     for num in nums:
    #         res = self.enqueue(num)
    #         if not res:
    #             result.append(max(self.items))
    #             self.dequeue()
    #             self.enqueue(num)
    #     result.append(max(self.items))  # 针对最后一个移动操作
    #     return result

    # a simple solution, but 11.84%
    # def maxSlidingWindow(self, nums, k):
    #     if not nums:
    #         return []
    #     result = []
    #     for i in range(len(nums) - k + 1):
    #         temp = max(nums[i : i + k])
    #         result.append(temp)
    #     return result

    # top voted solution, 83%
    def maxSlidingWindow(self, nums, k):
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                # Popped from d because d has elements and nums[d.top] < curr element
                d.pop()
            d.append(i)
            if d[0] == i - k:
                # Popped left from d because it's outside the window's leftmost (i-k)
                d.popleft()
            if i >= k - 1:
                out.append(nums[d[0]])
        return out

