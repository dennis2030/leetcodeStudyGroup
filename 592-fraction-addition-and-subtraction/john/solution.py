import fractions

class Fraction(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduction()

    def reduction(self):
        gcd = fractions.gcd(self.numerator, self.denominator)
        self.numerator /= gcd
        self.denominator /= gcd

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __str__(self):
        return '{}/{}'.format(self.numerator, self.denominator)

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        matches = re.findall(r'([\+-]?\d+)/(\d+)', expression)
        if not matches:
            raise Exception('invalid expression')
        frac = Fraction(0, 1)
        for match in matches:
            frac += Fraction(int(match[0]), int(match[1]))
        return str(frac)
