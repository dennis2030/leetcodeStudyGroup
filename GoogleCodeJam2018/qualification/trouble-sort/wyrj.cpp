#include <stdio.h>
#include <string.h>

int cmp(const void *a, const void *b) {
  return *(int *)a - *(int *)b;
}

void run() {
  int n;
  int ve[5000], vo[5000];
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    if (i % 2 == 0)
      scanf("%d", &ve[i / 2]);
    else
      scanf("%d", &vo[i / 2]);
  }
  qsort(ve, n / 2 + (n % 2 == 0 ? 0 : 1), sizeof(int), cmp);
  qsort(vo, n / 2, sizeof(int), cmp);
  for (int i = 0; i < n - 1; i++) {
    if ((i % 2 == 0 && ve[i / 2] > vo[i / 2]) ||
        (i % 2 == 1 && vo[i / 2] > ve[i / 2 + 1])) {
      printf(" %d\n", i);
      return;
    }
  }
  printf(" OK\n");
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
