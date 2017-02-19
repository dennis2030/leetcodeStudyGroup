class Solution {
public:
	int compareVersion(string version1, string version2) {
		string s;

		vector<string> sV1;
		istringstream issV1(version1);
		while (getline(issV1, s, '.')) {
			sV1.push_back(s);
		}

		vector<string> sV2;
		istringstream issV2(version2);
		while (getline(issV2, s, '.')) {
			sV2.push_back(s);
		}

		int sV1size = sV1.size();
		int sV2size = sV2.size();
		if (sV1size < sV2size) {
			for (int i = 0; i < sV2size - sV1size; i++) {
				sV1.push_back("0");
			}
		} else if (sV1size> sV2size) {
			for (int i = 0; i < sV1size- sV2size; i++) {
				sV2.push_back("0");
			}
		}

		for (int i = 0; i < sV1.size(); i++) {
			if (stoi(sV1[i],nullptr,0) > stoi(sV2[i],nullptr,0)) {
				return 1;
			} else if (stoi(sV1[i],nullptr,0) < stoi(sV2[i],nullptr,0)) {
				return -1;
			}
		}

		return 0;
	}
};
