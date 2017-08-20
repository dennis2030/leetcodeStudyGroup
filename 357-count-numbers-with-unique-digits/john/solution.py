class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def countExact(numDigits):
            if numDigits == 1:
                return 10
            if numDigits > 10:
                return 0

            numNums = 9
            for i in range(numDigits - 1):
                numChoices = 9 - i
                numNums *= numChoices
            return numNums

        if n == 0:
            return 1 # ???

        accum = 0
        for i in range(1, n + 1):
            accum += countExact(i)
        return accum
