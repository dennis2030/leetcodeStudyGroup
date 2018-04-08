import sys
import math

def go_gopher():
    a = int(raw_input())
    target_a = (int(a/3) + 1) * 3 if a % 3 != 0 else a
    target_move = (target_a - 9) / 3
    target_r = target_c = 3
    fill = [[False for x in xrange(1000)] for _ in xrange(1000)]

    move = 0
    max_iter = 1000
    while max_iter > 0:
        print '{0} {1}'.format(str(target_r), str(target_c))
        #sys.stderr.write('{0} {1}\n'.format(str(target_r), str(target_c)))
        sys.stdout.flush()

        r, c = [int(x) for x in raw_input().split(' ')]
        if r == c == 0:
            break
        if r == c == -1:
            sys.stderr.write('Got error')
            break
        fill[r][c] = True
        # check leftmost col to determine move target or not
        left_col = target_c - 1
        if move < target_move:
            if fill[target_r-1][left_col] and fill[target_r][left_col] and fill[target_r+1][left_col]:
                target_c += 1
                move += 1
        max_iter -= 1

def __main__():
    t = int(raw_input())
    for i in xrange(t):
        go_gopher()

if __name__ == '__main__':
    __main__()
