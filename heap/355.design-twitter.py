#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
import collections
import heapq

# top voted solution
# 使用列表, 94%
# 使用deque, 85%
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.tweets = collections.defaultdict(list)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        # self.tweets[userId].append((self.timer, tweetId))
        self.tweets[userId].appendleft((self.timer, tweetId))
        self.timer -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        followers = self.followees[userId]
        followers.add(userId) # 把自己加进去
        # tweets = [reversed(self.tweets[u]) for u in followers]
        tweets = [self.tweets[u] for u in followers]
        result = []
        for t in heapq.merge(*tweets):
            result.append(t[1])
            if len(result) == 10:
                break
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followees[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followees[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

