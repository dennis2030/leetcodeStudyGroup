class Solution(object):
	def ladderLength(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: int
		"""

		if endWord not in wordList:
			return 0

		length = 2
		front = set([beginWord])
		end = set([endWord])
		wordSet = set(wordList)
		wordSet.discard(beginWord)

		while front:
			NewWord = set()
			for word in front:
				for i in xrange(len(beginWord)):
					for c in 'abcdefghijklmnopqrstuvwxyz':
						newWord = word[:i] + c + word[i+1:]
						NewWord.add(newWord)
			front = wordSet & NewWord

			if front & end:
				return length

			length += 1

			if len(front) > len(end):
				front, end = end, front

			wordSet -= front

		return 0
