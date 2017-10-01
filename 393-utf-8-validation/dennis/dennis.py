class Solution(object):
    def getUtfLength(self, firstByte):        
        numOfOne = 0
        for i in xrange(5):
            if firstByte[i] == '0':
                return numOfOne
            numOfOne += 1
        return numOfOne
        
    def convertToLast8bit(self, data):
        return "{0:08b}".format(data)[-8:]
    
    def isValidFollowingByte(self, byte):
        return byte[0] == '1' and byte[1] == '0'
    
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        length = len(data)
        if length == 0:
            return True
        
        bytes = [self.convertToLast8bit(d) for d in data]
        
        curr_idx = 0
        while curr_idx < length:
            # first byte             
            utf8Length = self.getUtfLength(bytes[curr_idx])
            # not a valid first byte
            if utf8Length == 1 or utf8Length > 4 or curr_idx + utf8Length > length:                     
                return False
            
            for i in xrange(1, utf8Length):            
                if not self.isValidFollowingByte(bytes[curr_idx + i]):                                        
                    return False
            
            curr_idx += max(1, utf8Length)

        return True
