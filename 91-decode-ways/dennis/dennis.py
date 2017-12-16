class Solution(object):            
    def isValidDecoding(self, s):                 
        if len(s) == 0:
            return True
        int_s = int(s)        
        return str(int_s) == s and 1 <= int_s and int_s <= 26
    
    def calcComb(self, s):
        if s in self.decodingDict:
            return self.decodingDict[s]
        
        if len(s) <= 1 and self.isValidDecoding(s):
            return 1
        
        numOfDecodings = 0
        if self.isValidDecoding(s[:1]):            
            numOfDecodings += self.calcComb(s[1:])
        if self.isValidDecoding(s[:2]):            
            numOfDecodings += self.calcComb(s
                                            [2:])
        self.decodingDict[s] = numOfDecodings        
        return numOfDecodings
    
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """        
        if len(s) == 0:
            return 0
        self.decodingDict = {}
        return self.calcComb(s)
