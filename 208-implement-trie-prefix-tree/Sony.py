class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        def recursive_defauldict():
            return defaultdict(recursive_defauldict)
        self.trie_root = recursive_defauldict()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur_dict = self.trie_root
        for char in word:
            cur_dict = cur_dict[char]
        if 'words' not in cur_dict:
            cur_dict['words'] = word
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur_dict = self.trie_root
        for char in word:
            if char not in cur_dict:
                return False
            cur_dict = cur_dict[char]
        if 'words' in cur_dict and word in cur_dict['words']:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur_dict = self.trie_root
        for char in prefix:
            if char not in cur_dict:
                return False
            cur_dict = cur_dict[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
