class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = self._createEmptyNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self._root
        for idx, char in enumerate(word):
            if char not in curr['children']:
                curr['children'][char] = self._createEmptyNode()
            curr = curr['children'][char]
            curr['hasWord'] = curr['hasWord'] or (idx == len(word) - 1)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self._root
        for idx, char in enumerate(word):
            if char not in curr['children']:
                return False
            curr = curr['children'][char]
            if idx == len(word) - 1:
                return curr['hasWord']

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self._root
        for idx, char in enumerate(prefix):
            if char not in curr['children']:
                return False
            curr = curr['children'][char]
            if idx == len(prefix) - 1:
                return True

    def _createEmptyNode(self):
        return {
            'hasWord': False,
            'children': {}
        }


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
