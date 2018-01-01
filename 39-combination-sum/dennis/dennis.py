from collections import defaultdict
class Solution(object):
    
    def _init(self, candidates):
        self.target_dict = defaultdict(list)
        self.candidates = candidates
        
    def findComb(self, target):
        # already found the result
        if len(self.target_dict[target]) > 0:
            return self.target_dict[target]        
        if target == 0:
            return [{}]
        
        for candidate in self.candidates:
            if candidate > target:
                continue
            combs = self.findComb(target - candidate)
            
            for comb_dict in combs:
                # deeply copy a dict for creating a new dict
                tmp_dict = dict(comb_dict)
                if candidate not in tmp_dict:
                    tmp_dict[candidate] = 0                
                tmp_dict[candidate] += 1
                # already in ans
                if tmp_dict in self.target_dict[target]:
                    continue
                self.target_dict[target].append(tmp_dict)
                
        return self.target_dict[target]
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """        
        self._init(candidates)
        comb_dict_list = self.findComb(target)
        ans = []
        for comb_dict in comb_dict_list:
            one_sol = []
            for k,v in comb_dict.iteritems():
                for i in xrange(v):
                    one_sol.append(k)
            ans.append(one_sol)
        return ans
                    
