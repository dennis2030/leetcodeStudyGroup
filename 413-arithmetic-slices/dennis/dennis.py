class Solution(object):        
    def numOfSubseq(self, length):
        total = 0
        for i in xrange(3, length + 1):
            total += length - i + 1
        return total
            
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        
        diffs = [A[i] - A[i-1] for i in xrange(1, len(A))]
                
        last_diff = diffs[0]
        ans = 0
        current_length = 0
        for i in xrange(1, len(diffs)):
            diff = diffs[i]
            
            if diff == last_diff:
                current_length += 1
            elif current_length > 0:
                ans += self.numOfSubseq(current_length + 2)
                current_length = 0
            
            last_diff = diff     
            
        if current_length > 0:
            ans += self.numOfSubseq(current_length + 2)
        return ans
