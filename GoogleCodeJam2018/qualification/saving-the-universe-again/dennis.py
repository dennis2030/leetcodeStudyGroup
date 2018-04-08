def calc_damage(P):
    damage = 0
    curr = 1
    for c in P:
        if c == 'S':
            damage += curr
        elif c == 'C':
            curr *= 2
    return damage

def swap_CS(P, idx):
    swapped = list(P)
    swapped[idx + 1], swapped[idx] = swapped[idx], swapped[idx + 1]
    return ''.join(swapped)

def save_universe(D, P):
    D = int(D)
    num_hack = 0

    while calc_damage(P) > D:
        # find the last occurence of 'SC'
        idx = P.rfind('CS')
        # no 'SC' appear in string anymore
        if idx == -1:
            break
        num_hack += 1
        P = swap_CS(P, idx)

    return int(num_hack) if calc_damage(P) <= D else 'IMPOSSIBLE'

def __main__():
    t = int(raw_input())
    for i in xrange(t):
        D, P = raw_input().split(' ')
        print 'Case #{0}: {1}'.format(i + 1, save_universe(D, P))

if __name__ == '__main__':
    __main__()
