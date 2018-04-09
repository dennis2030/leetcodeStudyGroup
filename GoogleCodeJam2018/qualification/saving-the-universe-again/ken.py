T = int(raw_input())

for i in xrange(T):
    D, P = [s for s in raw_input().split(" ")]
    D = int(D)
    P = list(P)

    d = 1

    for c in P:
        if c == 'C':
            d *= 2
        elif c == 'S':
            D -= d

    ans = 'IMPOSSIBLE'
    if D >= 0:
        ans = '0'
    else:
        cnt = 0
        for j in xrange(len(P) - 1, -1, -1):
            if P[j] == 'C':
                k = j
                while k + 1 < len(P):
                    if D >= 0:
                        break
                    if P[k + 1] == 'C':
                        break
                    P[k] = 'S'
                    P[k + 1] = 'C'
                    D += (d / 2)
                    cnt += 1
                    k += 1
                d = d / 2
            if D >= 0:
                break
        if D >= 0:
            ans = str(cnt)

    print 'Case #%d: %s' % (i + 1, ans)
