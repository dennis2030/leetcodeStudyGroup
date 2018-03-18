#!/usr/bin/python3

import re

def solve(N):
    if N == 0:
        return 'INSOMNIA'

    digits = set()
    number = N
    while True:
        for digit in str(number):
            digits.add(digit)
        if len(digits) == 10:
            break
        number += N

    return number


def main():
    T = int(input())

    for idx in range(T):
        line = input()
        N = int(line)

        result = solve(N)

        print('Case #{}: {}'.format(idx + 1, result))

if __name__ == '__main__':
    main()
