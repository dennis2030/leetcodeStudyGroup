#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
        int t, n;
        cin >> t;
        for (int i = 1; i <= t; ++i) {
                cin >> n;
                vector<int> v;
                int input, tmp_n = n;
                while (tmp_n-- > 0) {
                        cin >> input;
                        v.push_back(input);
                }

                bool done = false;
                while(!done) {
                        done = true;
                        for (int j = 0; j < n-2; j++) {
                                if (v[j] > v[j+2]) {
                                        done = false;
                                        swap(v[j], v[j+2]);
                                }
                        }
                }

                bool isSorted = true;
                int errPosition = 0;
                for (int j = 0; j < n - 1; j++) {
                        if (v[j] > v[j+1]) {
                                isSorted = false;
                                errPosition = j;
                                break;
                        }
                }

                if (isSorted) {
                        cout << "Case #" << i << ": " << "OK" << endl;
                } else {
                        cout << "Case #" << i << ": " << errPosition << endl;
                }
        }

        return 0;
}
