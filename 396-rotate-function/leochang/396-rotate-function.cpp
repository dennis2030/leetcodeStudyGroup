class Solution {
public:
	int maxRotateFunction(vector<int>& A) {
		int size = A.size();
		long long sum = 0;
		long long weightedSum = 0;

		if (size == 0) return 0;

		for (int i = 0; i < size; ++i){
			sum += A[i];
			weightedSum += A[i] * i;
		}

		long long maxSum = weightedSum;

		for (int i = size -1; i > 0; --i) {
			weightedSum = weightedSum + sum - size * A[i];
			maxSum = max(maxSum, weightedSum);
		}

		return maxSum;
	}
};
