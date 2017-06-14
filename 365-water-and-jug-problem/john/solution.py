class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True
        if z > x + y:
            return False
        if 0 in [x, y]:
            return False

        import fractions
        gcd = fractions.gcd(x, y)

        return z % gcd == 0
