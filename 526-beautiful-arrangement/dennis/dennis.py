class Solution(object):
    def genCandidateList(self, N):
        self.candidate_list = []
        for pos in xrange(N):
            candidates = []
            for num in xrange(N):
                if ((num+1) % (pos+1) == 0) or ((pos+1) % (num+1) == 0): 
                    candidates.append(num)
            self.candidate_list.append(candidates)
                    
    def recursiveDP(self, N, used, idx):
        if idx == N:
            return 1
        
        total = 0        
        for num in self.candidate_list[idx]:
            if used[num-1]:
                continue
            nextUsed = list(used)
            nextUsed[num-1] = True
            total += self.recursiveDP(N, nextUsed, idx+1)
        return total
            
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.genCandidateList(N)    
        used = [False] * N
        return self.recursiveDP(N, used, 0)
