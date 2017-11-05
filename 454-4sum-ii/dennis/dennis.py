from collections import defaultdict

class Solution(object):
    def mergeDict(self, a_dict, b_dict):
        ans = 0        
        
        for key_a in a_dict:
            if -key_a in b_dict:
                ans += a_dict[key_a] * b_dict[-key_a]         
        return ans
    def twoSumCount(self, a_list, b_list, max_v, min_v):
        result_dict = defaultdict(int)
        for a in a_list:
            if a + b_list[-1] + max_v < 0:
                continue
            for b in b_list:
                tmp = a + b
                if tmp + min_v > 0:
                    break
                result_dict[a+b] += 1
        return result_dict
                
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        
        # only check 1 dict since their length are all the same
        if len(A) == 0:
            return 0
        
        # sort all list, O(nlogn)
        A.sort()
        B.sort()
        C.sort()
        D.sort()
        
        max_ab = A[-1] + B[-1]
        max_cd = C[-1] + D[-1]
        min_ab = A[0] + B[0]
        min_cd = C[0] + D[0]
        AB = self.twoSumCount(A, B, max_cd, min_cd)
        CD = self.twoSumCount(C, D, max_ab, min_ab)
        return self.mergeDict(AB, CD)
