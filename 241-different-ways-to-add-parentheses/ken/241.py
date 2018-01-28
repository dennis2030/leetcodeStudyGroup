class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        if '+' not in input and \
           '-' not in input and \
           '*' not in input:
           return [int(input)]

        ans = []

        for i in xrange(len(input)):
            c = input[i]

            if c != '+' and c != '-' and c != '*':
                continue

            v1 = self.diffWaysToCompute(input[:i])
            v2 = self.diffWaysToCompute(input[i+1:])

            for a in v1:
                for b in v2:
                    if c == '+':
                        ans.append(a + b)
                    elif c == '-':
                        ans.append(a - b)
                    elif c == '*':
                        ans.append(a * b)

        return ans
