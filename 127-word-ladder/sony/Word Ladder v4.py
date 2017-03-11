class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if (endWord not in wordList):
        	return 0

        word_len = len(beginWord)
        word_num = len(wordList)

        trans_map = dict()
        for word in wordList:
        	trans_map[word] = list()

        if beginWord in wordList:
        	begine_word_in_list = True
        else:
        	trans_map[beginWord] = list()
        	begine_word_in_list = False

        for i in xrange(word_len):
        	partial_word_map = dict()
        	for word in wordList:
        		partial_word = word[:i] + word[i + 1:]
        		if partial_word not in partial_word_map:
        			partial_word_map[partial_word] = list()
        		partial_word_map[partial_word].append(word)
        	for partial_word, word_list in partial_word_map.items():
        		for word in word_list:
        			trans_map[word] += word_list

        	if begine_word_in_list:
        		continue
        	partial_word = beginWord[:i] + beginWord[i + 1:]
        	if partial_word in partial_word_map:
        		trans_map[beginWord] += partial_word_map[partial_word]
        for key in trans_map:
        	trans_map[key] = set(trans_map[key])
        	trans_map[key].discard(key)

        visited = set()
        visited.add(beginWord)

        next_visit = list()
        now_visit = trans_map[beginWord]
        steps = 1
        word_found = False
        while steps < word_num:
        	if endWord in now_visit:
        		return steps + 1
        	visited = visited.union(now_visit)
        	for word in now_visit:
        		for next_word in trans_map[word]:
        			if next_word not in visited:
        				next_visit.append(next_word)
        	now_visit = set(next_visit)
        	next_visit = list()
        	steps += 1
        return 0




if __name__ == '__main__':
	sol = Solution()
	beginWord = "hit"
	endWord = "cog"
	wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
	print sol.ladderLength(beginWord, endWord, wordList)