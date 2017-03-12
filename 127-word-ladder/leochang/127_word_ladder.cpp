class Solution {
public:
	int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
		vector<string>::iterator it = find(wordList.begin(), wordList.end(), beginWord);
		if (it != wordList.end()) {
			wordList.erase(it);
		}
		int dist = 1;
		unordered_map<string, bool> isInList;
		for (vector<string>::iterator it = wordList.begin(); it != wordList.end();) {
			isInList[*it] = true;
			it = wordList.erase(it);  
		}

		queue<string> bfs;
		bfs.push(beginWord);

		while(!bfs.empty()) {
			int bfsSize = bfs.size();
			for (int n = 0; n < bfsSize; n++) {
				string word = bfs.front();
				bfs.pop();

				if (word == endWord) {
					return dist;
				}

				for(int i = 0; i < word.length(); i++) {
					char letter = word[i];
					for(char j = 'a'; j <= 'z'; j++) {
						if (letter != j) {
							word[i] = j;
							unordered_map<string, bool>::const_iterator it = isInList.find(word);
							if (it != isInList.end() && it->second) {
								bfs.push(word);
								isInList[word] = false;
							}
						}
						word[i] = letter;
					}
				}
			}
			dist++;
		}
		return 0;
	}
};
