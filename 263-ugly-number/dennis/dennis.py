class Solution(object):
    def divX(self, num, x):
        while num % x == 0 and num > 0:
            num /= x
        return num
    def isUgly(self, num):
        """                                                                                                                 
        :type num: int                                                                                                      
        :rtype: bool                                                                                                        
        """                                                                                                                 
        return 1 == self.divX(self.divX(self.divX(num, 2), 3), 5)
