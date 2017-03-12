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
        wordList.remove(endWord)

        visited = [False] * len(wordList)
        beginTodo = [(beginWord, 1)]
        endTodo = [(endWord, 1)]

        thisTodo = beginTodo
        thatTodo = endTodo
        while thisTodo:
            currWord, currLength = thisTodo.pop(0)

            for thatWord, thatLength in thatTodo:
                if self.isOneCharDiff(currWord, thatWord):
                    return currLength + thatLength

            for idx, iterWord in enumerate(wordList):
                if visited[idx]:
                    continue
                if self.isOneCharDiff(iterWord, currWord):
                    visited[idx] = True
                    thisTodo.append((iterWord, currLength + 1))

            if thisTodo is beginTodo:
                thisTodo = endTodo
                thatTodo = beginTodo
            else:
                thisTodo = beginTodo
                thatTodo = endTodo

        return 0
