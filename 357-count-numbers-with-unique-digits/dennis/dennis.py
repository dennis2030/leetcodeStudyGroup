class Solution(object):
    
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1        
        
        total = 9
        for i in xrange(1, n):
            total *= max((10 - i), 0)
        return total + self.countNumbersWithUniqueDigits(n-1)
