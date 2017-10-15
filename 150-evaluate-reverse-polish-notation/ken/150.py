class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        def isOP(token):
            if token == "+" or \
               token == "-" or \
               token == "*" or \
               token == "/":
               return True
            return False

        def OP(op, a, b):
            res = 0
            if token == "+":
                res = int(b) + int(a)
            elif token == "-":
                res = int(b) - int(a)
            elif token == "*":
                res = int(b) * int(a)
            elif token == "/":
                res = int(float(int(b)) / int(a))
            return res

        stack = []

        while len(tokens) > 0:
            token = tokens.pop(0)

            if isOP(token):
                a = stack.pop()
                b = stack.pop()
                res = OP(token, a, b)
                stack.append(str(res))
            else:
                stack.append(token)

        return int(stack[0])
