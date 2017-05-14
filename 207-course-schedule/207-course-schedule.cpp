class Solution {
public:
	bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
		vector<vector<int>> gragh(numCourses);
		vector<bool> visited(numCourses, false), path(numCourses, false);

		for (auto pre : prerequisites) {
			gragh[pre.second].push_back(pre.first);
		}

		for (int i = 0; i < numCourses; i++) {
			if (!visited[i] && dfs(i, gragh, visited, path)){
				return false;
			}
		}
		return true;
	}
private:
	bool dfs(int node, vector<vector<int>> &gragh, vector<bool> &visited, vector<bool> &path) {
		if (visited[node]) {
			return false;
		}

		visited[node] = true;
		path[node] = true;

		for (int neighbor : gragh[node]) {
			if (path[neighbor] || dfs(neighbor, gragh, visited, path)) {
				return true;
			}
		}

		return path[node] = false;
	}
};
