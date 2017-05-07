class Solution {
public:
	int numIslands(vector<vector<char>>& grid) {
		int ret = 0;
		if (0 != grid.size() && 0 != grid[0].size()) {
			for (int i = 0; i < grid.size(); i++) {
				for (int j = 0; j < grid[i].size(); j++) {
					if ('1' == grid[i][j]) {
						dfs(grid, i, j);
						ret++;
					}
				}
			}
		}
		return ret;
	}
private:
	void dfs(vector<vector<char>>& grid, int i, int j) {
		if (0 > i || grid.size() <= i || 0 > j || grid[i].size() <= j || '1' != grid[i][j]) {
			return;
		}
		grid[i][j] = '2';
		dfs(grid, i+1, j);
		dfs(grid, i, j+1);
		dfs(grid, i-1, j);
		dfs(grid, i, j-1);
	}
};
