class Solution(object):
    def isOneCharDiff(self, word1, word2):
        diffs = [1 if pair[0] != pair[1] else 0 for pair in zip(word1, word2)]
        return sum(diffs) == 1

    def genOneDiffWords(self, word):
        for idx in range(len(word)):
            for char in range(ord('a'), ord('z') + 1):
                yield word[:idx] + chr(char) + word[idx + 1:]

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        todo = [(beginWord, 1)]

        while todo:
            currWord, currLength = todo.pop(0)

            if self.isOneCharDiff(currWord, endWord):
                return currLength + 1

            for oneDiffWord in self.genOneDiffWords(currWord):
                if oneDiffWord not in wordSet:
                    continue

                wordSet.remove(oneDiffWord)
                todo.append((oneDiffWord, currLength + 1))

        return 0
