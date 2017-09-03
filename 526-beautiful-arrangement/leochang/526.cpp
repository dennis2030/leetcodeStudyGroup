class Solution {
public:
	int countArrangement(int N) {
		vector<bool> used(N+1, false);
		return dfs(N, 1, used);
	}
	int count;
private:
	int dfs(int N, int index, vector<bool> &used) {
		if (N + 1 == index) {
			count++;
			return 1;
		}

		int ret = 0;

		for (int i = 1; i <= N; i++) {
			if (!used[i] && (0 == i % index || 0 == index % i)) {
				used[i] = true;
				ret += dfs(N, index+1, used);
				used[i] = false;
			}
		}

		return ret;
	}
};

