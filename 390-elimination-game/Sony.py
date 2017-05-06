class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        multiply = 2
        remaining = 0
        remain_nums = int(n / 2)
        reverse = True

        while remain_nums > 1:
            if reverse:
                if remain_nums % 2 == 1:
                    if remaining == 0:
                        remaininig = multiply
                    else:
                        remaining = remaining + multiply
                else:
                    if remaining == 0:
                        remaining = remaining + multiply

                reverse = False
            else:
                if remaining != 0:
                    remaining = remaining + multiply
                reverse = True

            multiply *= 2
            remain_nums = int(remain_nums / 2)
            
        return remaining if remaining != 0 else multiply if multiply <= n else multiply / 2

if __name__ == '__main__':
    sol = Solution()
    n = 8
    print sol.lastRemaining(n)
    
