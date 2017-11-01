/**
 * Initialize your data structure here.
 */
var Twitter = function() {
    this.tweetMap = new Map();
    this.followMap = new Map();
    this.counter = 0;
};

/**
 * Compose a new tweet. 
 * @param {number} userId 
 * @param {number} tweetId
 * @return {void}
 */
Twitter.prototype.postTweet = function(userId, tweetId) {
    const array = this.tweetMap.get(userId) || [];
    array.push({ tweetId:tweetId, uId:this.counter++ });
    this.tweetMap.set(userId, array);
};

/**
 * Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. 
 * @param {number} userId
 * @return {number[]}
 */
Twitter.prototype.getNewsFeed = function(userId) {
    const heap = new BinaryHeap((a, b) => { return a.uId < b.uId ? 1 : -1; });
    let array = [userId].concat(Array.from(this.followMap.get(userId) || new Set()));
    array.forEach(followee => {
        if (!this.tweetMap.has(followee)) return;
        this.tweetMap.get(followee).forEach(tweet => {
            heap.push(tweet);
            if (heap.size() > 10) heap.pop();
        });
    });
    return heap.toArray().map(tweet => { return tweet.tweetId; });
};

/**
 * Follower follows a followee. If the operation is invalid, it should be a no-op. 
 * @param {number} followerId 
 * @param {number} followeeId
 * @return {void}
 */
Twitter.prototype.follow = function(followerId, followeeId) {
    if (followerId === followeeId) return;
    const set = this.followMap.get(followerId) || new Set();
    set.add(followeeId);
    this.followMap.set(followerId, set);
};

/**
 * Follower unfollows a followee. If the operation is invalid, it should be a no-op. 
 * @param {number} followerId 
 * @param {number} followeeId
 * @return {void}
 */
Twitter.prototype.unfollow = function(followerId, followeeId) {
    const set = this.followMap.get(followerId) || new Set();
    set.delete(followeeId);
    this.followMap.set(followerId, set);    
};

/** 
 * Your Twitter object will be instantiated and called as such:
 * var obj = Object.create(Twitter).createNew()
 * obj.postTweet(userId,tweetId)
 * var param_2 = obj.getNewsFeed(userId)
 * obj.follow(followerId,followeeId)
 * obj.unfollow(followerId,followeeId)
 */

function _parent(i) {
  return i >> 1;
}

function _right(i) {
  return (i << 1) + 1;
}

function _left(i) {
  return (i << 1);
}

function heapify(arr, i, comp) {
  let l = _left(i);
  let r = _right(i);
  let largest;

  if (l < arr.length && comp(arr[i], arr[l]) < 0)
    largest = l;
  else
    largest = i;
  if (r < arr.length && comp(arr[largest], arr[r]) < 0)
    largest = r;

  if (largest !== i) {
    let t = arr[i];
    arr[i] = arr[largest];
    arr[largest] = t;
    return heapify(arr, largest, comp);
  }
}

class BinaryHeap {
  constructor(comp) {
    this.comp = comp;
    this.collection = [];
  }

  clear() {
    this.collection = [];
  }

  from(array) {
    this.collection = array.slice(0);
    for (let i = ~~(array.length / 2); i >= 0; --i)
      heapify(this.collection, i, this.comp);
    return this;
  }

  toArray() {
    return this.collection.sort(this.comp);
  }

  size() {
    return this.collection.length;
  }

  get length() {
    return this.collection.length;
  }

  push(value) {
    this.collection.push(value);
    const arr = this.collection;
    for (let i = arr.length - 1; i > 0 && this.comp(arr[_parent(i)], arr[i]) < 0; i = _parent(i)) {
      const t = arr[i];
      arr[i] = arr[_parent(i)];
      arr[_parent(i)] = t;
    }
    return this;
  };

  top() {
    return this.collection[0];
  }

  pop() {
    let ret = this.collection[0];
    if (1 < this.collection.length) {
      this.collection[0] = this.collection.pop();
      heapify(this.collection, 0, this.comp);
    } else {
      this.collection.pop();
    }

    return ret;
  };
}
