class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        slices = []
        skip = 0
        for idx in range(len(A) - 2):
            if skip > 0:
                skip -= 1
                continue

            diff = A[idx + 1] - A[idx]
            sliceSize = 2
            for jdx in range(idx + 1, len(A) - 1):
                if A[jdx + 1] - A[jdx] == diff:
                    sliceSize += 1
                else:
                    break

            if sliceSize == 2:
                continue

            slices.append(sliceSize)
            skip = sliceSize - 2

        result = 0
        for sliceSize in slices:
            n = sliceSize - 2
            result += (1 + n) * n // 2

        return result
