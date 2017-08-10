class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        import fractions
        expression_len = len(expression)
        def find_fraction(idx):
            slash_idx = idx + 1
            while True:
                if expression[slash_idx] == '/':
                    break
                slash_idx += 1
            num_idx = slash_idx + 1
            while num_idx < expression_len:
                if expression[num_idx] == '+' or expression[num_idx] == '-':
                    break
                num_idx += 1
            return int(expression[idx:slash_idx]), int(expression[slash_idx + 1:num_idx]), num_idx
        numerator, denominator, new_idx = find_fraction(0)
        while new_idx < expression_len:
            operator = expression[new_idx]
            new_numerator, new_denominator, new_idx = find_fraction(new_idx + 1)
            if operator == '+':
                numerator = numerator * new_denominator + new_numerator * denominator
            else:
                numerator = numerator * new_denominator - new_numerator * denominator
            denominator = denominator * new_denominator
            gcd = fractions.gcd(numerator, denominator)
            numerator /= gcd
            denominator /= gcd
        return '{0}/{1}'.format(numerator, denominator)

if __name__ == '__main__':

    sol = Solution()
    expression = "-1/2+1/3"

    print sol.fractionAddition(expression)