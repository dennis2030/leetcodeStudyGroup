#!/usr/bin/python3

import re

def solve(S):
    flips = 0
    for idx in range(len(S)):
        if idx == len(S) - 1:
            if S[idx] == '-':
                flips += 1
        elif S[idx] != S[idx + 1]:
            flips += 1
    return flips


def main():
    T = int(input())

    for idx in range(T):
        line = input()
        S = line

        result = solve(S)

        print('Case #{}: {}'.format(idx + 1, result))

if __name__ == '__main__':
    main()
