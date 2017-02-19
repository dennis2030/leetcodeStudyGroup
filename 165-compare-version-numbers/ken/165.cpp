class Solution {
public:
    int compareVersion(string version1, string version2) {
        vector<int> v1;
        vector<int> v2;

        v1 = ParseVersion(version1);
        v2 = ParseVersion(version2);

        int Length = (v1.size() < v2.size()) ? v2.size() : v1.size();

        for (int i = v1.size(); i < Length; i++) {
            v1.push_back(0);
        }

        for (int i = v2.size(); i < Length; i++) {
            v2.push_back(0);
        }

        for (int i = 0; i < Length; i++) {
            if (v1[i] > v2[i]) {
                return 1;
            } else if (v1[i] < v2[i]) {
                return -1;
            }
        }

        return 0;
    }

    vector<int> ParseVersion(const string &version) {
        vector<int> versionList;
    	size_t found = 0;
        size_t previous_found = -1;

        while (true) {
            found = version.find(".", previous_found + 1);

            if (found == std::string::npos) {
                int Token = stoi(version.substr(previous_found + 1));

                versionList.push_back(Token);
                break;
            }

            int Token = stoi(version.substr(previous_found + 1, found - previous_found));

            versionList.push_back(Token);
            previous_found = found;
        }

        return versionList;
    }
};