class Solution {
public:
    int minMutation(string start, string end, vector<string>& bank) {
		int dist = 0;
		unordered_map<string, bool> isInList;
		for (vector<string>::iterator it = bank.begin(); it != bank.end();) {
			isInList[*it] = true;
			it = bank.erase(it);  
		}

		queue<string> bfs;
		bfs.push(start);

		while(!bfs.empty()) {
			int bfsSize = bfs.size();
			for (int n = 0; n < bfsSize; n++) {
				string word = bfs.front();
				bfs.pop();

				if (word == end) {
					return dist;
				}

				for(int i = 0; i < word.length(); i++) {
					char letter = word[i];
					for(auto j : string("ATGC")) {
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
		return -1;
    }
};
