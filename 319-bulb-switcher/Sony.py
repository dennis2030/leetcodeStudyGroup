class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        return int(sqrt(n))




if __name__ == '__main__':

    sol = Solution()


    n = 10
    print sol.bulbSwitch(n)