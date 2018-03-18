#include <stdio.h>
#include <string.h>

int main()
{
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
      int K, C, S;
      scanf("%d %d %d", &K, &C, &S);
      printf("Case #%d:", t);
      int need = K / C + (K % C == 0 ? 0 : 1);
      if (need > S) {
          printf(" IMPOSSIBLE\n");
          continue;
      }
      unsigned long long index = 0;
      int count = need * C;
      for (int i = 0; i < count; i++) {
          index = index * K + (i >= K ? 0 : i);
          if ((i + 1) % C == 0) {
              printf(" %llu", index + 1);
              index = 0;
          }
      }
      printf("\n");
  }
  return 0;
}
