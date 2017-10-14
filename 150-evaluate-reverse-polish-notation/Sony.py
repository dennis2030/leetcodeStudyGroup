class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        import re
        operator_pat = re.compile(r'^[\+\-\*\/]$')
        nums_stack = [0]
        for token in tokens:
            print nums_stack, token
            if operator_pat.match(token):
                num2 = nums_stack.pop()
                num1 = nums_stack.pop()
                if token == "+":
                    new_num = num1 + num2
                elif token == '-':
                    new_num = num1 - num2
                elif token == '*':
                    new_num = num1 * num2
                else:
                    new_num = int(float(num1) / num2)
                nums_stack.append(new_num)
            else:
                nums_stack.append(int(token))
        return nums_stack.pop()

if __name__ == '__main__':

    sol = Solution()
    tokens = ["2", "1", "+", "3", "*"]
    tokens = ["4", "13", "5", "/", "+"]
    tokens = ["3","-4","+"]
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    #tokens = []
    print sol.evalRPN(tokens)