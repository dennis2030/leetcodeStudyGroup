class Solution {
public:
	int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
		int sum = 0;
		int lowest = 0;
		for (int i = 0; i < gas.size(); i++) {
			sum += gas[i] - cost[i];
			lowest = lowest < sum ? lowest : sum;
		}

		if (sum < 0) {
			return -1;
		}

		int start = 0;
		int end = gas.size() - 1;
		while (lowest < sum) {
			lowest = lowest + gas[end] - cost[end];
			start = end;
			end--;
		}
		return start;
	}
};
