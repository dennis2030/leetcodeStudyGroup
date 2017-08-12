/**
 * Initialize your data structure here.
 */
var RandomizedSet = function() {
    this.hash = {};
    this.arr = [];
};

/**
 * Inserts a value to the set. Returns true if the set did not already contain the specified element. 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function(val) {
    if (this.hash.hasOwnProperty(val)) return false;
    this.hash[val] = this.arr.length;
    this.arr.push(val);
    return true;
};

/**
 * Removes a value from the set. Returns true if the set contained the specified element. 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function(val) {
    if (!this.hash.hasOwnProperty(val)) return false;
    let index = this.hash[val];
    delete this.hash[val];
    let value = this.arr.pop();
    if (index < this.arr.length) {
        this.arr[index] = value;
        this.hash[value] = index;
    }
    return true;
};

/**
 * Get a random element from the set.
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function() {
    let len = this.arr.length;
    return this.arr[Math.floor(Math.random() * len)];
};

/** 
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = Object.create(RandomizedSet).createNew()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
