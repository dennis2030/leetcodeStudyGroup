from collections import defaultdict
class Post(object):
    order = 0
    def __init__(self, id):
        self._id = id
        self._order = Post.order
        Post.order += 1
    def __repr__(self):
        return str(self._id) + ' ' + str(self._order)
    
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweets[userId].insert(0, Post(tweetId))
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        # tweet_list is list(list)
        tweet_list = self.tweets[userId][:10]
        for f_id in self.follows[userId]:
            tweet_list += self.tweets[f_id][:10]
        
        tweet_list = sorted(tweet_list, key=lambda post: post._order, reverse=True)
        
        return [post._id for post in tweet_list[:10]]
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId not in self.follows[followerId]:
            return
        self.follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
