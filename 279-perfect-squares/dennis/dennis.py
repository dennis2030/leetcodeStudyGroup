class Solution(object):
    def find_max_square(self, n):
        i = 1
        while i*i <= n:
            i += 1
        return i - 1
        
    def recursive(self, n, current_count, min_count):
        
        if self.result[n] != None:            
            return self.result[n]
        
        if current_count > min_count:            
            self.result[n] = min_count + 1
            return self.result[n]
        
        max_square = self.find_max_square(n)
        min = n
        for i in reversed(xrange(1, max_square+1)):            
            sq = i*i
            now = self.recursive(n - sq, current_count + 1, min) + 1
            if now < min:
                min = now                
                
        self.result[n] = min
        
        return min
            
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """        
        
        self.result = [None] * (n+1)
        max_square = self.find_max_square(n)
        for i in xrange(1, max_square+1):
            self.result[i*i] = 1
        return self.recursive(n, 1, n)
                
        
