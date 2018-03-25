#include <iostream>
using namespace std;

int main() {
        int t, n;
        cin >> t;
        for (int i = 1; i <= t; ++i) {
                bool count[10] = {false};
                cin >> n;
                for (int j = 1; j <= 100; j ++) {
                        int nn = n * j;
                        while(nn != 0) {
                                count[nn%10] = true;
                                nn /= 10;
                        }
                        int k = 0;
                        for (k = 0; k < 10; k++) {
                                if (!count[k]) break;
                        }
                        if (k == 10) {
                                cout << "Case #" << i << ": " << n*j << endl;
                                break;
                        }
                }

                for (int j = 0; j < 10; j++) {
                        if (!count[j]) {
                                cout << "Case #" << i << ": " << "INSOMNIA" << endl;
                                break;
                        }
                }
        }

        return 0;
}
