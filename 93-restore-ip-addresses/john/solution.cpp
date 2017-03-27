class Solution {
public:
    bool isValidNum(const string &part) {
        if (part.at(0) == '0' && part.size() > 1) {
            return false;
        }

        if (part.size() > 3) {
            return false;
        }

        int num = 0;
        sscanf(part.c_str(), "%d", &num);

        return (num <= 255);
    }

    void fillDots(vector<string> &results, const string &s, vector<int> dots) {
        if (dots.size() == 4) {
            dots.push_back(s.size());
            vector<string> parts;
            for (int i = 0; i < 4; ++i) {
                parts.push_back(s.substr(dots.at(i), dots.at(i + 1) - dots.at(i)));
            }

            if (isValidNum(parts.back())) {
                results.push_back(parts.at(0) + "." + parts.at(1) + "." + parts.at(2) + "." + parts.at(3));
            }
            return;
        }

        int start = dots.back();
        for (int i = start + 1; i < s.size(); ++i) {
            string part = s.substr(start, i - start);

            if (!isValidNum(part)) {
                break;
            }

            dots.push_back(i);
            fillDots(results, s, dots);
            dots.pop_back();
        }
    }

    vector<string> restoreIpAddresses(string s) {
        vector<string> results;
        vector<int> dots = {0};

        fillDots(results, s, dots);

        return results;
    }
};
