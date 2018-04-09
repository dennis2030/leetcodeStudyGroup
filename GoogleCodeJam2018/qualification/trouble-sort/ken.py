T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())
    l = [int(s) for s in raw_input().split(" ")]

    even = l[0:][::2]
    odd = l[1:][::2]
    even.sort()
    odd.sort()

    ans = 'OK'
    for j in xrange(len(odd)):
        if even[j] > odd[j]:
            ans = str(2 * j)
            break

        if j + 1 < len(even) and odd[j] > even[j + 1]:
            ans = str(2 * j + 1)
            break

    print 'Case #%d: %s' % (i + 1, ans)
