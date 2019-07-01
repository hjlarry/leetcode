#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (38.00%)
# Likes:    1746
# Dislikes: 105
# Total Accepted:    164.7K
# Total Submissions: 428.4K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
# 
# Example:
# 
# 
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7] 
# Explanation: 
# 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty
# array.
# 
# Follow up:
# Could you solve it in linear time?
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
