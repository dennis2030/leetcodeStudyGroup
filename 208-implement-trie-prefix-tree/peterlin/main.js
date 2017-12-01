/**
 * Initialize your data structure here.
 */
var TrieNode = function() {
    this.map = new Map();
}

var Trie = function() {
    this.root = new TrieNode();
};

/**
 * Inserts a word into the trie. 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let node = this.root;
    for (let i=0; i<word.length; ++i) {
        const k = word[i];
        if (!node.map.has(k)) {
            node.map.set(k, new TrieNode());
        }
        node = node.map.get(k);
    }
    node.map.set(0, true);
};

/**
 * Returns if the word is in the trie. 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let node = this.root;
    for (let i=0; i<word.length; ++i) {
        if (!node.map.has(word[i])) return false;
        node = node.map.get(word[i]);
    }
    return node.map.has(0);
};

/**
 * Returns if there is any word in the trie that starts with the given prefix. 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let node = this.root;
    for (let i=0; i<prefix.length; ++i) {
        if (!node.map.has(prefix[i])) return false;
        node = node.map.get(prefix[i]);
    }
    return true;
};

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = Object.create(Trie).createNew()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
