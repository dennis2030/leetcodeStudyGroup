class Solution(object):
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

		words = set([beginWord])
		length = 1
		while words:
			NewWord = set()
			for word in words:
				for i in xrange(len(beginWord)):
					for c in 'abcdefghijklmnopqrstuvwxyz':
						newWord = word[:i] + c + word[i+1:]
						NewWord.add(newWord)
			words = wordSet & NewWord

			length += 1
			if endWord in words:
				return length

			wordSet -= NewWord

		return 0
