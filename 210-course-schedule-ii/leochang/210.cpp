class Solution {
public:
    vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {
		vector<vector<int>> gragh(numCourses);
        vector<int> ans;
		vector<bool> visited(numCourses, false), path(numCourses, false);

		for (auto pre : prerequisites) {
			gragh[pre.second].push_back(pre.first);
		}

		for (int i = 0; i < numCourses; i++) {
			if (!visited[i] && dfs(i, gragh, visited, path, ans)){
				return {};
			}
		}
    reverse(ans.begin(), ans.end());
		return ans;
    }
private:
	bool dfs(int node, vector<vector<int>> &gragh, vector<bool> &visited, vector<bool> &path, vector<int>& ans) {
		if (visited[node]) {
			return false;
		}

		visited[node] = true;
		path[node] = true;

		for (int neighbor : gragh[node]) {
			if (path[neighbor] || dfs(neighbor, gragh, visited, path, ans)) {
				return true;
			}
		}
        
    ans.push_back(node);
		return path[node] = false;
	}
};
