class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isSquare(num):
            sqrt = math.sqrt(num)
            return sqrt == int(sqrt)

        def searchNumSteps(curr, groups):
            for run in groups[1]:
                if (curr - run) in groups[1]:
                    return 2
            for run in groups[1]:
                if (curr - run) in groups[2]:
                    return 3
            return 4

        groups = {}
        for numStep in range(4):
            numStep += 1 # [1, 4]
            groups[numStep] = set()

        for curr in range(n):
            curr += 1 # [1, n]
            if isSquare(curr):
                numStep = 1
            else:
                numStep = searchNumSteps(curr, groups)

            groups[numStep].add(curr)

        return numStep
