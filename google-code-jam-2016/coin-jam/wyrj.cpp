#include <stdio.h>
#include <string.h>

void add(char s[], int index) {
    if (index < 0) {
        printf("RRRRRR");
        return;
    }
    if (s[index] == '0') {
        s[index] = '1';
    } else {
        s[index] = '0';
        add(s, index - 1);
    }
}

bool test11(char s[], int len) {
    int v = 0;
    for (int i = 0; i < len; i++) {
        if (s[i] == '1') {
            if (i % 2 == 0) v += 1;
            else v -= 1;
        }
    }
    return v % 11 == 0;
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
      int N, J;
      scanf("%d %d", &N, &J);
      char s[33];
      s[N] = '\0';
      s[0] = '1';
      s[N - 1] = '1';
      for (int i = 1; i < N - 1; i++) s[i] = '0';
      printf("Case #%d:\n", t);
      printf("%s 3 4 5 6 7 8 9 10 11\n", s); //N must be even
      int count = 1;
      while (count < J) {
          add(s, N - 2);
          if (test11(s, N)) {
              printf("%s 3 4 5 6 7 8 9 10 11\n", s);
              count += 1;
          }
      }
  }
  return 0;
}
