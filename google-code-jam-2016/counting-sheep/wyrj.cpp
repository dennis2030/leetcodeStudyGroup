// Example program
#include <iostream>
#include <string>

bool check(bool record[]) {
    for (int i = 0; i < 10; i++) {
        if (record[i] == false) return false;
    }
    return true;
}

int main()
{
  int T, N;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
      scanf("%d", &N);
      if (N == 0) {
          printf("Case #%d: INSOMNIA\n", t);
          continue;
      }
      bool record[10] = {false};
      int n = 0;
      while (!check(record)) {
          n += N;
          int p = 1;
          while (n >= p) {
              record[n / p % 10] = true;
              p *= 10;
          }
      }
      printf("Case #%d: %d\n", t, n);
  }
  return 0;
}
