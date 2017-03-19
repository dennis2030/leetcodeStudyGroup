class Solution {
public:
	int maximalSquare(vector<vector<char> >& matrix) {
		char maxLength = 0;
		for (int i = 0; i < matrix.size(); ++i) {
			for (int j = 0; j < matrix[i].size(); ++j) {
				matrix[i][j] = matrix[i][j] - '0';
				if (i > 0 && j > 0 && matrix[i][j] == 1) {
					matrix[i][j] = min(min(matrix[i-1][j], matrix[i][j-1]), matrix[i-1][j-1]) + 1;
				}
				maxLength = max(maxLength, matrix[i][j]);
			}
		}
		return (int)(maxLength * maxLength);
	}
};
