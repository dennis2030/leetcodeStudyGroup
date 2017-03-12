class Solution(object):
    def isOneCharDiff(self, word1, word2):
        diffs = [1 if pair[0] != pair[1] else 0 for pair in zip(word1, word2)]
        return sum(diffs) == 1

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        visited = [False] * len(wordList)
        todo = [(beginWord, 1)]

        while todo:
            currWord, currLength = todo.pop(0)

            if self.isOneCharDiff(currWord, endWord):
                return currLength + 1

            for idx, iterWord in enumerate(wordList):
                if visited[idx]:
                    continue
                if self.isOneCharDiff(iterWord, currWord):
                    visited[idx] = True
                    todo.append((iterWord, currLength + 1))

        return 0
