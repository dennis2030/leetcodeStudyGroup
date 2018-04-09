import sys

t = int(raw_input())

for i in xrange(t):
    a = int(raw_input())

    area = [[0 for k in xrange(1000)] for j in xrange(1000)]

    si = 10
    sj = 10
    for j in xrange(1000):
        sys.stdout.write('%d %d\n' % (si, sj))
        sys.stdout.flush()

        i1, j1 = [int(s) for s in raw_input().split(" ")]
        if i1 == 0 and j1 == 0:
            break
        if i1 == -1 and j1 == -1:
            break
        else:
            area[i1][j1] = 1

            r = 0
            if area[si - 1][sj - 1] + area[si - 1][sj] + area[si - 1][sj + 1] == 3:
                r = 1
                if area[si][sj - 1] + area[si][sj] + area[si][sj + 1] == 3:
                    r = 2
                    if area[si + 1][sj - 1] + area[si + 1][sj] + area[si + 1][sj + 1] == 3:
                        r = 3

            si += r
