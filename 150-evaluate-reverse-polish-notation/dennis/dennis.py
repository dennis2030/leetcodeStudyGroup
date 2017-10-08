class Solution(object):
    def doOperation(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return int(float(a)/b) # I thinks this problem is not defined well
        
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = ['+', '-', '*', '/']
        stack = []
        
        for s in tokens:
            if s in operators:
                b = stack.pop()
                a = stack.pop()
                ele = self.doOperation(a, b, s)
            else:
                ele = int(s)
            stack.append(ele)            
        return stack[0]
