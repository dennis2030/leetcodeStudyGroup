class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        if num == 0:
            return [0]
        if num == 1:
            return [0,1]
            
        now = 0
        next = 2
        
        result = []
        result.append(0)
        result.append(1)
        
        for i in xrange(2, num + 1):
            if i == next:
                # only leading 1
                result.append(1)
                now = next
                next = next * 2
            else:
                result.append(result[i - now] + 1)
        return result
