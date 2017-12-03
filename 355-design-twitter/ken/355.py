class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.feeds = []
        self.follows = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """

        self.feeds.append((userId, tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """

        ret = []
        targetUser = set()
        targetUser.add(userId)

        if userId in self.follows:
            targetUser |= self.follows[userId]

        for feed in self.feeds[::-1]:
            if feed[0] in targetUser:
                ret.append(feed[1])

            if len(ret) == 10:
                break

        return ret

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

        if followerId not in self.follows or followeeId not in self.follows[followerId]:
            return
        self.follows[followerId].remove(followeeId)
