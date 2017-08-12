class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        class Fraction(object):
            def __init__(self, numerator, denominator):
                self.numerator = numerator
                self.denominator = denominator

            def add(self, other):
                self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
                self.denominator = self.denominator * other.denominator

            def reduce(self):
                def gcd(a, b):
                    while b:
                        a, b = b, a%b
                    return a

                g = gcd(self.numerator, self.denominator)
                self.denominator /= g
                self.numerator /= g

            def __str__(self):
                return "%d/%d" % (self.numerator, self.denominator)

        def parseToFractions(expression):
            import re

            fractions = []
            parsed = re.findall("(\+?-?\d+/\d+)", expression)
            for tmp in parsed:
                numerator, denominator = tmp.split("/")
                fractions.append(Fraction(int(numerator), int(denominator)))

            return fractions

        fractions = parseToFractions(expression)
        result = Fraction(0, 1)

        for fraction in fractions:
            result.add(fraction)
        result.reduce()

        return str(result)


a = Solution()
print a.fractionAddition("1/2+1/3-1/4")

