class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """       
        # for sys.maxint
        import sys
        ugly_idx = [0] * len(primes)
        ugly_nums = []
        
        ugly_nums.append(1)
        
        for i in xrange(1, n):
            next_ugly = sys.maxint
            min_idx = -1
            for j in xrange(len(primes)):
                candidate = ugly_nums[ugly_idx[j]] * primes[j]                
                
                # If duplicated candidate, jump to next candidate
                if candidate == ugly_nums[i-1]:
                    ugly_idx[j] += 1
                    candidate = ugly_nums[ugly_idx[j]] * primes[j]
                    
                if candidate < next_ugly:
                    min_idx = j
                    next_ugly = candidate
            
            ugly_idx[min_idx] += 1
            ugly_nums.append(next_ugly)
            
        return ugly_nums[n-1]
