class Twitter {
public:
    /** Initialize your data structure here. */
    Twitter() {
        time = 0;
    }
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
        tweets[userId].emplace_back(make_pair(time, tweetId));
        time++;
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
        vector<int> ret;
        vector<vector<pair<int,int>>> tmpTweets;
        
        tmpTweets.push_back(tweets[userId]);
        for(auto user: following[userId]) {
            tmpTweets.push_back(tweets[user]);
        }
        
        while (10 > ret.size()) {
            int maxTime = INT_MIN;
            int tmpT = 0;
            
            for (int i = 0; i < tmpTweets.size(); i++) {
                if(0 < tmpTweets[i].size() && tmpTweets[i].back().first > maxTime) {
                    maxTime = tmpTweets[i].back().first;
                    tmpT = i;
                }
            }
            
            if (maxTime == INT_MIN) {
                break;
            } else {
                if(ret.size() == 0 || tmpTweets[tmpT].back().second != ret.back()) {
                    ret.push_back(tmpTweets[tmpT].back().second);
                }
                tmpTweets[tmpT].pop_back();
            }
        }
        
        return ret;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int followerId, int followeeId) {
        if (followerId != followeeId) {
            following[followerId].insert(followeeId);
        }
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
        following[followerId].erase(followeeId);
    }
private:
    unordered_map<int, vector<pair<int,int>>> tweets;
    unordered_map<int, unordered_set<int>> following;
    int time;
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * vector<int> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */
