from collections import deque
class Solution(object):
    def findComb(self, k, n, start_idx):        
        if k < 0 or n < 0:
            return False        
        if n == 0 and k == 0:
            return [[]]
        
        ans = []
        for i in xrange(start_idx, 10):
            combs = self.findComb(k - 1, n - i, i + 1)                        
            if combs == False:
                continue                
            for comb in combs:
                ans.append([i] + comb)
        
        return ans
            
            
            
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """        
        return self.findComb(k, n, 1)
            
