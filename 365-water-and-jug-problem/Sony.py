class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z in (0, x, y, x + y):
            return True

        bigger = max(x, y)
        smaller = min(x, y)

        if smaller == 0:
            return False

        diff = bigger - smaller
        while True:
            if diff == z:
                return True
            while diff >= smaller:
                diff -= smaller
                if diff == z:
                    return True
            if diff > 0:
                if diff + bigger == z:
                    return True
                diff = bigger - (smaller - diff)
            else:
                break

        return True if z == diff else False


if __name__ == '__main__':

    sol = Solution()
    x = 2
    y = 0
    z = 1

    print sol.canMeasureWater(x, y, z)