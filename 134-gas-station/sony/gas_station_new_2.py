#!/usr/bin/env python

#https://leetcode.com/problems/gas-station/


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        list_len = len(gas)
        earn_list = list()
        min_balance = 0
        balance = 0
        answer = -1

        for i in xrange(list_len):
            earn_list.append(gas[i] - cost[i])
            balance = balance + earn_list[i]
            if balance < min_balance:
                min_balance = balance
        if balance >= 0:
            if min_balance >= 0:
                answer = 0
            else:
                for i in xrange(list_len):
                    min_balance = min_balance - earn_list[i]
                    if min_balance >= 0:
                        answer = (i + 1) % list_len
                        break

        print answer

if __name__ == '__main__':
    sol = Solution()
    gas = [2, 4]
    cost = [3, 4]
    sol.canCompleteCircuit(gas, cost)
