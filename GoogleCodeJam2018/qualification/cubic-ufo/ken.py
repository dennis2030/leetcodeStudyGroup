import math

T = int(raw_input())

for i in xrange(T):
    A = float(raw_input())

    a = 0
    b = math.pi / 4
    t = (a + b) / 2

    cnt = 0

    while True:
        t = (a + b) / 2
        if A < math.sin(t) + math.cos(t):
            b = t
        elif A > math.sin(t) + math.cos(t):
            a = t
        else:
            break

        cnt += 1

    x1 = 0.5 * math.sin(t)
    y1 = 0.5 * math.cos(t)
    x2 = 0.5 * math.cos(t)
    y2 = -0.5 * math.sin(t)

    print 'Case #%d:' % (i + 1)
    print '%.8f %.8f 0' % (x1, y1)
    print '%.8f %.8f 0' % (x2, y2)
    print '0 0 0.5'
