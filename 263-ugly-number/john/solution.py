class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False

        def divideUp(dividend, divisor):
            while dividend % divisor == 0:
                dividend //= divisor
            return dividend

        dividend = num
        dividend = divideUp(dividend, 2)
        dividend = divideUp(dividend, 3)
        dividend = divideUp(dividend, 5)

        return (dividend == 1)
