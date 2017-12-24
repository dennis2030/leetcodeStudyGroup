class TrieNode {
public:
    TrieNode() : isWord(false){
        next = vector<TrieNode*>(26, NULL);
    }
    bool isWord;
    vector<TrieNode*> next;
};

class Trie {
public:
    /** Initialize your data structure here. */
    Trie() {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode* node = root;
        for(auto c : word){
            if(!node->next[c-'a']) {
                node->next[c-'a'] = new TrieNode();
            }
            node = node->next[c -'a'];
        }
        node->isWord = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode* node = root;
        for(auto c : word) {
            if(!node->next[c-'a']) return false;
            node = node->next[c-'a'];
        }
        return node->isWord;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TrieNode* node = root;
        for(auto c : prefix) {
            if(!node->next[c-'a']) return false;
            node = node->next[c-'a'];
        }
        return true;
    }
private:
    TrieNode* root;
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * bool param_2 = obj.search(word);
 * bool param_3 = obj.startsWith(prefix);
 */
