class User(object):
    def __init__(self, userId):
        self.followeeSet = set()
        self.tweets = list()
        self.userId = userId
        
    def follow(self, user):
        self.followeeSet.add(user)

    def unfollow(self, user):
        self.followeeSet.discard(user)
        
    def tweet(self, seq, postId):
        self.tweets.append((seq, postId))

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.userDict = dict() #uid to user object
        self.seq = 0
        
    def getUser(self, userId):
        if userId in self.userDict:
            return self.userDict[userId]
        user = User(userId)
        self.userDict[userId] = user
        return user
        
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        user = self.getUser(userId)
        user.tweet(self.seq, tweetId)
        self.seq += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        tweetsList = []
        resultList = []
        user = self.getUser(userId)
        if len(user.tweets) > 0:
            tweetsList.append(user.tweets[-10:])
        for followee in user.followeeSet:
            if followee.userId != userId and len(followee.tweets) > 0:
                tweetsList.append(followee.tweets[-11:])
        
        while len(resultList) < 10:
            if len(tweetsList) == 0:
                break
            tweetsIdx = None
            maxSeq = -1
            for idx, tweets in enumerate(tweetsList):
                if tweets[-1][0] > maxSeq:
                    maxSeq = tweets[-1][0]
                    tweetsIdx = idx
            targetTweets = tweetsList[tweetsIdx]
            tweet = targetTweets.pop()[1]
            if len(targetTweets) == 0:
                tweetsList.pop(tweetsIdx)
            resultList.append(tweet)
        return resultList
            
    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        follower = self.getUser(followerId)
        followee = self.getUser(followeeId)
        follower.follow(followee)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        follower = self.getUser(followerId)
        followee = self.getUser(followeeId)
        follower.unfollow(followee)
