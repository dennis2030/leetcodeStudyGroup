class Solution(object):
        def canCompleteCircuit(self, gas, cost):
            """
            :type gas: List[int]
            :type cost: List[int]
            :rtype: int
            """
            diff_list = []
            sum_ = 0
            arr_max_len = len(gas)
            last_max_minus = 0
            last_max_minus_idx = -1

            for i in xrange(arr_max_len):
                diff = gas[i] - cost[i]

            if diff <= last_max_minus:
                last_max_minus = diff
                last_max_minus_idx = i
                sum_ += diff
                diff_list.append(diff)
            if sum_ < 0:
                return -1
            for i in xrange(arr_max_len):
                idx = (last_max_minus_idx + i) % arr_max_len
                if diff_list[idx] >= 0:
                    return idx
