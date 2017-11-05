class Solution {
public:
	int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
		int size = A.size(), ans = 0;
		unordered_map<int, int> sum;

		for (int i = 0; i < size; i++) {
			for (int j = 0; j < size; j++) {
				sum[A[i] + B[j]]++;
			}
		}

		for (int i = 0; i < size; i++) {
			for (int j = 0; j < size; j++) {
				int tmp_sum = C[i] + D[j];
				if (sum.end() != sum.find(-tmp_sum)) ans += sum[-tmp_sum];
			}
		}

		return ans;
	}
};
