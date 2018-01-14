class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        ans = []
        candidates = [i for i in range(1, 10)]
        
        def rec(cur, idx):
            if len(cur) == k:
                if sum(cur) == n:
                    ans.append(list(cur))
                return
            
            for i in xrange(idx, len(candidates)):
                c = candidates[i]
                cur.append(c)
                rec(cur, i + 1)
                cur.pop()
            
        
        rec([], 0)
        
        return ans
    
