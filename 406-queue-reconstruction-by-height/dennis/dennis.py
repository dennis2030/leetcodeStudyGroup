class Solution(object):    
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        people = sorted(people, key=lambda p: p[0]*1100 - p[1], reverse=True)
        
        while len(people) > 0:
            h_now = people[0][0] # first height
            end_idx = 1 # initialize to 1 to prevent end_idx == 0
            for idx in xrange(len(people)):
                if h_now != people[idx][0]:
                    end_idx = idx
                    break
            
            for idx in xrange(end_idx):
                p = people[idx]
                result.insert(p[1], p)
            
            people = people[end_idx:]
            
        return result
