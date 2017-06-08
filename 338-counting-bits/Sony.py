#!/usr/bin/env python
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        num += 1
        result_list = [0] * num

        try:
            current_base = 0
            next_base = 2
            result_list[1] = 1
            for i in xrange(2, num):
                if i == next_base:
                    result_list[i] = 1
                    current_base = next_base
                    next_base *= 2
                else:
                    result_list[i] = 1 + result_list[i - current_base]

            return result_list
        except:
            return [0]

if __name__ == '__main__':
    sol = Solution()

    num = 5
    print sol.countBits(num)
