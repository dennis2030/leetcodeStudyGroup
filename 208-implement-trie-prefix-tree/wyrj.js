/**
 * Initialize your data structure here.
 */
var Trie = function() {
    this.map = {};
    this.isEnd = false;
};

/**
 * Inserts a word into the trie. 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    if (word.length === 0) {
        this.isEnd = true;
        return;
    }
    let a = word[0]
    if (!this.map[a]) {
        this.map[a] = new Trie();
    }
    this.map[a].insert(word.substr(1));
};

/**
 * Returns if the word is in the trie. 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    if (word.length === 0) {
        return this.isEnd;
    }
    let a = word[0];
    return this.map[a] ? this.map[a].search(word.substr(1)) : false;
};

/**
 * Returns if there is any word in the trie that starts with the given prefix. 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    if (prefix.length === 0) {
        return true;
    }
    let a = prefix[0];
    return this.map[a] ? this.map[a].startsWith(prefix.substr(1)) : false;
};

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = Object.create(Trie).createNew()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
