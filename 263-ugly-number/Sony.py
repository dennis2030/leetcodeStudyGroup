class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def getSimplifiedNum(num, divisor):
            while num % divisor == 0:
                num //= divisor
            return num

        if num <= 0:
            return False

        num = getSimplifiedNum(num, 2)
        num = getSimplifiedNum(num, 3)
        num = getSimplifiedNum(num, 5)
        
        return 1 == num
