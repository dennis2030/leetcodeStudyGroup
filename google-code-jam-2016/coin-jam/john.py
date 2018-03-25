#!/usr/bin/python3

import re

class Bad(Exception):
    pass

def generate(N):
    bits = N - 2
    for binary in range(2 ** bits):
        fmt = '1{{:0{}b}}1'.format(bits)
        yield fmt.format(binary)

def translate(coin, base):
    addup = 0
    for power, digit in enumerate(reversed(coin)):
        addup += int(digit) * (base ** power)
    return addup

def find(coin):
    attempts = (2, 3, 5, 7, 11, 13, 17, 19)
    divisors = []
    for base in range(2, 10 + 1):
        num = translate(coin, base)
        for attempt in attempts:
            if num % attempt == 0:
                divisors.append(attempt)
                break
        else:
            raise Bad()
    return divisors

def solve(N, J):
    jamcoins = []
    for coin in generate(N):
        try:
            divisors = find(coin)
            jamcoins.append((coin, divisors))
        except Bad:
            pass
        if len(jamcoins) >= J:
            break
    else:
        return []
    return jamcoins

def main():
    T = int(input())

    for idx in range(T):
        line = input()
        tokens = re.split(' ', line)
        N = int(tokens[0])
        J = int(tokens[1])

        result = solve(N, J)

        print('Case #{}:'.format(idx + 1))
        for jamcoin, divisors in result:
            print('{} {}'.format(jamcoin, ' '.join([str(divisor) for divisor in divisors])))

if __name__ == '__main__':
    main()
