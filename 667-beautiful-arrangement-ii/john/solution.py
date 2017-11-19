class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        def genDiff():
            if k % 2 == 0:
                sign = -1
            else:
                sign = +1

            for diff in range(k):
                yield (diff + 1) * sign
                sign *= -1

            for idx in range(n - k - 1):
                yield +1

        start = 1 + k // 2
        result = [start]
        for diff in genDiff():
            result.append(result[-1] + diff)
        return result
