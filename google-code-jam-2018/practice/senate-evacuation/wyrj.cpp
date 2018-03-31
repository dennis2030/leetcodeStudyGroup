#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Party {
    int count;
    char name;
};

int cmp(const void *a, const void *b) {
    struct Party* pa = (struct Party*)a;
    struct Party* pb = (struct Party*)b;
    return pb->count - pa->count;
}

void run() {
    int N, sum = 0;
    struct Party P[26];
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        P[i].name = 65 + i;
        scanf("%d", &P[i].count);
        sum += P[i].count;
    }
    qsort(P, N, sizeof(struct Party), cmp);
    int index = 0;
    if (sum % 2 == 1) printf(" ");
    while (sum > 0) {
        if (sum % 2 == 0) printf(" ");
        printf("%c", P[index].name);
        P[index].count -= 1;
        if (index == N - 1 || P[index + 1].count <= P[index].count) index = 0;
        else index += 1;
        sum -= 1;
    }
    printf("\n");
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%d:", i);
        run();
    }
    return 0;
}
