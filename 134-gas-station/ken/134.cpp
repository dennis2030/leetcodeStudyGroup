class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int N = gas.size();
        int Gas = 0;
        int Start = 0;
        int Current = 0;

        while (true) {
        	if (Gas >= 0) {
        		Gas += gas[Current] - cost[Current];
        		Current = (Current + 1) % N;        		
        	} else {
        		Start = (Start - 1 + N) % N;
        		Gas += gas[Start] - cost[Start];
        	}

        	if (Current == Start) {
        		break;
        	}
        }

        if (Gas >= 0) {
        	return Start;
        }

        return -1;
    }
};