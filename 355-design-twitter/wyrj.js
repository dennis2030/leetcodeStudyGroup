/**
 * Initialize your data structure here.
 */
var Twitter = function() {
    this.followMap = {};
    this.postMap = {};
    this.postCount = 0;
};

/**
 * Compose a new tweet. 
 * @param {number} userId 
 * @param {number} tweetId
 * @return {void}
 */
Twitter.prototype.postTweet = function(userId, tweetId) {
    if (!this.postMap[userId]) {
        this.postMap[userId] = [];
    }
    this.postMap[userId].push({id: tweetId, time: this.postCount++});
};

/**
 * Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. 
 * @param {number} userId
 * @return {number[]}
 */
Twitter.prototype.getNewsFeed = function(userId) {
    let news = this.postMap[userId] || [];
    const followees = this.followMap[userId] || [];
    followees.forEach((followee) => {
        news = news.concat(this.postMap[followee] || []);
    })
    news.sort((l, r) => (r.time - l.time));
    if (news.length > 10) news.length = 10;
    return news.map((post) => post.id);
};

/**
 * Follower follows a followee. If the operation is invalid, it should be a no-op. 
 * @param {number} followerId 
 * @param {number} followeeId
 * @return {void}
 */
Twitter.prototype.follow = function(followerId, followeeId) {
    if (followerId === followeeId) return;
    if (!this.followMap[followerId]) {
        this.followMap[followerId] = [];
    }
    let index = this.followMap[followerId].indexOf(followeeId);
    if (index < 0) {
        this.followMap[followerId].push(followeeId);
    }
};

/**
 * Follower unfollows a followee. If the operation is invalid, it should be a no-op. 
 * @param {number} followerId 
 * @param {number} followeeId
 * @return {void}
 */
Twitter.prototype.unfollow = function(followerId, followeeId) {
    if (!this.followMap[followerId]) return;
    let index = this.followMap[followerId].indexOf(followeeId);
    if (index >= 0) {
        this.followMap[followerId].splice(index, 1);
    }
};

/** 
 * Your Twitter object will be instantiated and called as such:
 * var obj = Object.create(Twitter).createNew()
 * obj.postTweet(userId,tweetId)
 * var param_2 = obj.getNewsFeed(userId)
 * obj.follow(followerId,followeeId)
 * obj.unfollow(followerId,followeeId)
 */
