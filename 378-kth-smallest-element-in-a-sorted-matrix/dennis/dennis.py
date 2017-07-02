from Queue import PriorityQueue
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        pq = PriorityQueue()
        for i in xrange(n):
            pq.put((matrix[i][0], int(i), 0))
        
        now = 0
        while True:            
            (ele, r_idx, c_idx) = pq.get()            
            now += 1
            if now == k:
                return ele
            if c_idx + 1 < n:                
                pq.put((matrix[r_idx][c_idx+1], r_idx, c_idx+1))        
