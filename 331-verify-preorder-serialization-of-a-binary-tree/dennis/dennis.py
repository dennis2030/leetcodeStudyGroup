class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        max_afford = 1
        
        for ele in preorder.split(','):
            max_afford -= 1
            if max_afford < 0:
                return False
            if ele != '#':
                max_afford += 2
            
        
        return False if (max_afford != 0) else True
