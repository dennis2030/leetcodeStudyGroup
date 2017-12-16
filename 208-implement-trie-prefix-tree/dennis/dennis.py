class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for c in word:
            current = current.setdefault(c, {})
        current['has_word'] = True

    def _traverse(self, word):
        current = self.root
        for c in word:
            if c not in current:
                return False
            current = current[c]
        return current
    
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self._traverse(word)
        return current != False and 'has_word' in current
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self._traverse(prefix) != False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
