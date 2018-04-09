#include <iostream>
#include <unordered_map>
#include <algorithm>

using namespace std;

int c(unordered_map<int, int> &table, int d, int &all_damage, int &big_damage) {
        int move_front = 0, count = 0;
        while (d < all_damage) {
                if (table[big_damage] > 0) {
                        all_damage = all_damage - (big_damage / 2);
                        table[big_damage]--;
                        move_front++;
                        count++;
                } else {
                        big_damage /= 2;
                        table[big_damage] += move_front;
                        move_front = 0;
                }
        }
        return count;
}

void dp(unordered_map<int, int> &table, string &p, int &all_damage, int &big_damage) {
        int damage = 1;
        for (int i = 0; i < p.length(); i++) {
                if (p[i] == 'S') {
                        if (table.find(damage) == table.end()) {
                                table.emplace(damage, 1);
                        } else {
                                table[damage]++;
                        }
                        all_damage += damage;
                        big_damage = damage;
                } else {
                        damage *= 2;
                }
        }
}

int main() {
        int t, d;
        cin >> t;
        for (int i = 1; i <= t; ++i) {
                cin >> d;
                string p;
                cin >> p;

                if (d < count(p.begin(), p.end(), 'S')) {
                        cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
                } else {
                        int change = 0, all_damage = 0, big_damage = 0;
                        unordered_map<int, int> table;
                        dp(table, p, all_damage, big_damage);
                        cout << "Case #" << i << ": " << c(table, d, all_damage, big_damage) << endl;
                }
        }

        return 0;
}
