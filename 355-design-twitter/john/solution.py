class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweetSeq = 0
        self.tweets = {}
        self.follows = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.tweetSeq, tweetId))
        self.tweetSeq += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        searchUserIds = set([userId])
        if userId in self.follows:
            searchUserIds |= self.follows[userId]

        allFollowedTweets = []
        for searchUserId in searchUserIds:
            if searchUserId not in self.tweets:
                continue
            allFollowedTweets.extend(self.tweets[searchUserId])
        allFollowedTweets.sort(reverse=True)
        return [tweet[1] for tweet in allFollowedTweets[:10]]


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.follows:
            return
        if followeeId not in self.follows[followerId]:
            return
        self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
