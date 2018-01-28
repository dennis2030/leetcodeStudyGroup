import re
class Solution(object):        
    def doOperator(self, first, second, op):
        if op == '*':
            return first * second
        elif op == '+':
            return first + second
        elif op == '-':
            return first - second
                
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        ans = []
        
        nums = re.split('[*+-]', input)        
        if (len(nums) == 1):
            return [int(nums[0])]
        
        for i in xrange(len(input)):
            if input[i] not in '*+-':
                continue
                
            first_combs = self.diffWaysToCompute(input[0:i])
            second_combs = self.diffWaysToCompute(input[i+1:len(input)])            
            # handling all combinations
            op = input[i]
            for first in first_combs:
                for second in second_combs:
                    ans.append(self.doOperator(int(first), int(second), op))
        
        return ans
