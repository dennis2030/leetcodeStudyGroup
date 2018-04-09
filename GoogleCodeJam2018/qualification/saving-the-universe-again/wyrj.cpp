#include <stdio.h>
#include <string.h>

void run() {
  int d;
  char p[30] = {'\0'};
  scanf("%d %s", &d, p);

  int s = 1;
  int count = 0;
  int damage = 0;
  int arr[30] = {0};
  int idx = 0;
  int len = strlen(p);
  for (int i=0; i<len; i++) {
    if (p[i] == 'C') {
      s *= 2;
      idx += 1;
    } else {
      count += 1;
      arr[idx] += 1;
      damage += s;
    }
  }
  if (count > d) {
    printf(" IMPOSSIBLE\n");
    return;
  }
  count = 0;
  s /= 2;
  while (damage > d) {
    if (p[idx] == 0) {
      idx -= 1;
      s /= 2;
      continue;
    }
    p[idx] -= 1;
    p[idx - 1] += 1;
    count += 1;
    damage -= s;
  } 
  printf(" %d\n", count);
}

int main() {
  int t;
  scanf("%d", &t);
  for (int i=1; i<=t; i++) {
    printf("Case #%d:", i);
    run();
  }
  return 0;
}
