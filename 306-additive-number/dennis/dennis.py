class Solution(object):    
    def digitLen(self, num):
        if num == 0:
            return 1
        return int(math.log10(num))+1
    def checkNum(self, num, prev_prev, prev):
        if len(num) == 0:
            return True
        
        # not a valid num (e.g., 03 is not a valid input number)
        if len(prev) != self.digitLen(int(prev)) or len(prev_prev) != self.digitLen(int(prev_prev)):
            return False
        
        added = int(prev_prev) + int(prev)
        num_len = len(str(added))
        
        if len(num) < num_len or int(num[:num_len]) != added:
            return False
        
        return self.checkNum(num[num_len:], prev, str(added))
        
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        for i in xrange(1, len(num)):
            for j in xrange(i + 1, len(num)):
                prev_prev = num[:i]
                prev = num[i:j]                
                if self.checkNum(num[j:], prev_prev, prev):
                    return True
        return False
        
        
