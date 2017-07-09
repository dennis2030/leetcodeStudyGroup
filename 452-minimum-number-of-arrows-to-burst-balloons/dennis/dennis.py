class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x : x[1])
        
        num_of_arrows = 0
        popped = [False] * len(points)
        last_popped_idx = 0
        
        for idx in xrange(len(points)):
            if True == popped[idx]:
                continue
            end = points[idx][1]
            for compare_idx in xrange(last_popped_idx, len(points)):
                start = points[compare_idx][0]                
                if True == popped[compare_idx]:
                    continue
                if start <= end:
                    popped[compare_idx] = True
                    last_popped_idx = compare_idx
                else:
                    break
                
            num_of_arrows += 1
            
        return num_of_arrows
                    
        
