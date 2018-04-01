import operator
from collections import defaultdict

def find_max_options(senate_dict):
    max_v = -1
    max_keys = []
    for i in xrange(26):
        key_now = chr(i+65)
        value_now = senate_dict[key_now]
        if value_now == max_v:
            max_keys.append(key_now)
        elif value_now > max_v:
            max_keys = [key_now]
            max_v = value_now

    # double the keys to avoid only 1 max key
    return max_keys + max_keys 

def evacuate(senate_list):
    senate_dict = defaultdict(int)
    ans = []

    # convert senates to dict
    for i in xrange(len(senate_list)):
        senate_dict[chr(i+65)] = senate_list[i]

    total_senate = sum(senate_list)
    # case even, evacuate 1 person first
    if total_senate % 2 == 1:
        max_options = find_max_options(senate_dict)
        ans.append(max_options[0])
        senate_dict[max_options[0]] -= 1
        total_senate -= 1

    while total_senate > 0:
        max_options = find_max_options(senate_dict)
        ans_this_round = ''
        for i in xrange(2):
            option = max_options[i]
            ans_this_round += option
            senate_dict[option] -= 1
            total_senate -= 1
        ans.append(ans_this_round)

    return ' '.join(ans)

def __main__():
    t = int(raw_input())
    for i in xrange(t):
        N = int(raw_input())
        senate_list = [int(x) for x in raw_input().split(' ')]
        print 'Case #{0}: {1}'.format(i + 1, evacuate(senate_list))

if __name__ == '__main__':
    __main__()
