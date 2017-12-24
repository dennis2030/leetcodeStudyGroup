class Trie(object):
    class Node(object):
        def __init__(self):
            self.val = False
            self.next = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = self.Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.node
        for c in word:
            if c not in node.next:
                node.next[c] = self.Node()

            node = node.next[c]

        node.val = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        hasValue = True
        node = self.node
        for c in word:
            if c not in node.next:
                hasValue = False
                break

            node = node.next[c]

        if hasValue and node.val:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        hasValue = True
        node = self.node
        for c in prefix:
            if c not in node.next:
                hasValue = False
                break

            node = node.next[c]

        return hasValue

