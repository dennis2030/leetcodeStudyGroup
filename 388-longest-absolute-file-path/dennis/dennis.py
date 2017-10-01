class Solution(object):
             
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """                
        level_length = [0] * (input.count('\n') + 1)
        max_length = 0        
        
        for path in input.split('\n'):
            level = path.count('\t')
            length = len(path.lstrip('\t'))            
            level_length[level] = length
            
            is_file = path.count('.')            
            if is_file:
                current_length = sum(level_length[0:level + 1]) + level # plus the length of slash
                max_length = max(max_length, current_length)
                
        return max_length
