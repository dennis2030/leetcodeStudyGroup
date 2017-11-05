class Solution {
public:
	int leastBricks(vector<vector<int>>& wall) {
		if (0 == wall.size()) return 0;

		int maxWidth = 0;
		unordered_map<int, int> edges;

		for (auto row : wall) {
			int sum = 0;
			for (int i = 0; i < row.size(); i++) {
				sum += row[i];
				edges[sum]++;
			}
			maxWidth = sum;
		}

		int maxHit = 0;
		edges.erase(maxWidth);
		for (auto &edge : edges) {
			maxHit = max(maxHit, edge.second);
		}

		return wall.size() - maxHit;
	}
};
