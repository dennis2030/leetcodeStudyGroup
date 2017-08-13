
import re
class FracNumber:    
    def __init__(self, numerator, denominator):
        self._numerator = numerator
        self._denominator = denominator
    def __add__(self, other):        
        tmp_numerator = other._denominator * self._numerator + self._denominator * other._numerator
        tmp_denominator = self._denominator * other._denominator
        return FracNumber(tmp_numerator, tmp_denominator)    
    
    def reduce(self):        
        from fractions import gcd
        _gcd = gcd(self._numerator, self._denominator)        
        tmp_numerator = int(self._numerator / _gcd)
        tmp_denominator = int(self._denominator / _gcd)        
        return FracNumber(tmp_numerator, tmp_denominator)
    
    def __str__(self):
        return str(self._numerator) + '/' + str(self._denominator)
        
        
class Solution(object):                
    def readInput(self, input_str):
        matched_items = re.findall('[\+-]?\d+/\d+', input_str)
        return [FracNumber(int(numerator), int(denominator)) for numerator, denominator in (item.split('/') for item in matched_items)]
        
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        frac_nums = self.readInput(expression)
        result = FracNumber(0, 1)
        for f in frac_nums:
            result += f        
        return str(result.reduce())
        
