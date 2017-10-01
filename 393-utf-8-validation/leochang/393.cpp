class Solution {
public:
	bool validUtf8(vector<int>& data) {
		int byteCounts = 0;
		for (int i = 0; i < data.size(); i++) {
			if (data[i] < 128) {
				if (byteCounts > 0) return false;
				continue;
			}
			if (data[i] >= 128 && data[i] < 192) {
				byteCounts--;
				continue;
			}
			if (byteCounts > 0 || data[i] > 247) return false;
			if (data[i] >= 240) {
				byteCounts+=3;
				continue;
			}
			if (data[i] >= 224) {
				byteCounts+=2;
				continue;
			}
			if (data[i] >= 192) {
				byteCounts+=1;
				continue;
			}
		}
		return 0 == byteCounts;
	}
};
