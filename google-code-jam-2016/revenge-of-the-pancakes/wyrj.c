#include <stdio.h>
#include <string.h>

int main()
{
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
      char S[101] = {0};
      scanf("%s", &S);
      char c = S[0];
      int len = strlen(S), count = 0;
      for (int i = 1; i < len; i++) {
          if (c != S[i]) {
              count += 1;
              c = S[i];
          }
      }
      if (c != '+') {
          count += 1;
      }
      printf("Case #%d: %d\n", t, count);
  }
  return 0;
}
