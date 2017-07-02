class Solution {
public:
	bool isValidSudoku(vector<vector<char>>& board) {
		int size = board.size();
		bool isExist[128] = {false};
		for (int i = 0; i < size; i++) {
			for (int j = 0; j < size; j++) {
				if ('.' != board[i][j] && !isExist[board[i][j]]) {
					isExist[board[i][j]] = true;
				} else if ('.' != board[i][j] && isExist[board[i][j]]){
					return false;
				}
			}
			fill(begin(isExist), end(isExist), false);
		}
		for (int j = 0; j < size; j++) {
			for (int i = 0; i < size; i++) {
				if ('.' != board[i][j] && !isExist[board[i][j]]) {
					isExist[board[i][j]] = true;
				} else if ('.' != board[i][j] && isExist[board[i][j]]){
					return false;
				}
			}
			fill(begin(isExist), end(isExist), false);
		}
		for (int i = 0; i < size; i+=3) {
			for (int j = 0; j < size; j+=3) {
				for (int k = i; k < i+3; k++) {
					for (int m = j; m < j+3; m++) {
						if ('.' != board[k][m] && !isExist[board[k][m]]) {
							isExist[board[k][m]] = true;
						} else if ('.' != board[k][m] && isExist[board[k][m]]){
							return false;
						}
					}
				}
				fill(begin(isExist), end(isExist), false);
			}
		}
		return true;
	}
};
