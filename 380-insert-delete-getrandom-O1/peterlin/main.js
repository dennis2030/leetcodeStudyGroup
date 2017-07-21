/**
 * Initialize your data structure here.
 */
var RandomizedSet = function() {
    this.keys = new Map;
    this.values = new Map;
};

/**
 * Inserts a value to the set. Returns true if the set did not already contain the specified element. 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function(val) {
    if (this.keys.has(val)) {
        return false;
    }
    var length = this.keys.size;
    this.keys.set(val, length);
    this.values.set(length, val);
    return true;
};

/**
 * Removes a value from the set. Returns true if the set contained the specified element. 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function(val) {
    if (this.keys.has(val)) {
        var length = this.keys.size;
        if (this.keys.get(val) < length-1) {
            this.values.set(this.keys.get(val), this.values.get(length-1));
            this.keys.set(this.values.get(length-1), this.keys.get(val));
        }
        this.keys.delete(val);
        this.values.delete(length-1);
        return true;
    }
    return false;
};

/**
 * Get a random element from the set.
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function() {
    var length = this.keys.size;
    var i = Math.floor(Math.random()*length);
    return this.values.get(i);
};

/** 
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = Object.create(RandomizedSet).createNew()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
