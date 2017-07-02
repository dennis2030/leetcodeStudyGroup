class Solution {
public:
	int kthSmallest(vector<vector<int>>& matrix, int k) {
		int size = matrix.size();
		priority_queue<int, std::vector<int>, std::greater<int> > pQueue;

		if (k == size * size) {
			return matrix[size-1][size-1];
		}

		for (int i = 0; i < size; i++) {
			for (int j = 0; j < size; j++) {
				pQueue.push(matrix[i][j]);
			}
		}

		for (int i = 0; i < k-1; i++) {
			pQueue.pop();
		}
		return pQueue.top();
	}
};
