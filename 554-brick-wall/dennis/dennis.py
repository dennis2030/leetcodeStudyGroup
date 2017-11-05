from collections import defaultdict
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        
        if len(wall) == 0:
            return 0
        
        sum_dict = defaultdict(int)
        
        for row in wall:
            current_width = 0
            for w in row:
                current_width += w
                sum_dict[current_width] += 1
            sum_dict[current_width] = 0 # eliminate the edge
                    
        key, value = max(sum_dict.iteritems(), key=lambda x: x[1])
        
        return len(wall) - value
        
                
