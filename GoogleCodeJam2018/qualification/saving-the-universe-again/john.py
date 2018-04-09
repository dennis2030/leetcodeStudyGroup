#!/usr/bin/python3

import re


def calc_damage(codes):
    power = 1
    total_damage = 0
    for code in codes:
        if code == 'C':
            power *= 2
        elif code == 'S':
            total_damage += power
        else:
            raise Exception()
    return total_damage


def do_hack(codes, position):
    front = codes[:position]
    middle = codes[position:position + 2]
    back = codes[position + 2:]
    return front + ''.join(reversed(middle)) + back


def solve(D, P):
    num_hacks = 0
    codes = P
    while calc_damage(codes) > D:
        if 'CS' not in codes:
            return 'IMPOSSIBLE'
        position = codes.rindex('CS')
        codes = do_hack(codes, position)
        num_hacks += 1

    return num_hacks


def main():
    T = int(input())

    for idx in range(T):
        line = input()
        tokens = re.split(' ', line)
        D = int(tokens[0])
        P = tokens[1]

        result = solve(D, P)

        print('Case #{}: {}'.format(idx + 1, result))

if __name__ == '__main__':
    main()
