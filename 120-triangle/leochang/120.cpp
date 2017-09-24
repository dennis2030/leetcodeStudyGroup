class Solution {
public:
	int minimumTotal(vector<vector<int>>& triangle) {
		int rows = triangle.size();
		vector<int> minPathSum(triangle.back());
		for (int i = rows - 2; i >= 0; i--) {
			for (int j = 0; j <= i; j++) {
				minPathSum[j] = min(minPathSum[j], minPathSum[j + 1]) +triangle[i][j];
			}
		}
		return minPathSum[0];
	}
};
