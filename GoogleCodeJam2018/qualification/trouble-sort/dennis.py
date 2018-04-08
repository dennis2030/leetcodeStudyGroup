def trouble_sort(N, L):
    odd_list = L[::2]
    even_list = L[1::2]

    odd_list.sort()
    even_list.sort()

    now = odd_list[0]
    idx = 1
    while idx < N:
        if idx % 2 == 1:
            comp = even_list[int(idx/2)]
        else:
            comp = odd_list[int(idx/2)]
        if now > comp:
            return str(idx - 1)
        now = comp
        idx += 1
    return 'OK'

def __main__():
    t = int(raw_input())
    for i in xrange(t):
        N = int(raw_input())
        L = [int(x) for x in raw_input().split(' ')]
        print 'Case #{0}: {1}'.format(i + 1, trouble_sort(N, L))

if __name__ == '__main__':
    __main__()
