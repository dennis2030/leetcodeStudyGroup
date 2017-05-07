class Solution(object):
    def left(self, n):
        if n <= 2:
            return n
        return 2 * self.right(n/2)
    def right(self, n):
        if n <=2:
            return 1
        # case odd
        if n % 2 == 1:
            return 2 * self.left(n/2)
        return 2 * self.left(n/2) - 1
        
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.left(n)
                
