class Solution {
public:
	int lengthLongestPath(string input) {
		int maxLen = 0;
		map <int, int> len;

		for(int i = 0; i < input.size(); i++){
			int count = 0, dirLevel = 1;
			bool isFile = false;
			while(input[i] == '\t' && i < input.size()){
				dirLevel++;
				i++;
			}
			while(input[i] != '\n' && i < input.size()){
				if (input[i] == '.') isFile = true;
				count++;
				i++;
			}
			if (isFile) {
				maxLen = max(maxLen, len[dirLevel - 1] + count);
			} else {
				len[dirLevel] = len[dirLevel - 1] + count + 1;
			}
		}
		return maxLen;
	}
};
