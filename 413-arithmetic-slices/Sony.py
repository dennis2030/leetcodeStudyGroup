class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        len_A = len(A)
        idx_1 = 0
        idx_2 = 1
        result = 0
        while idx_2 < len_A:
            diff = A[idx_2] - A[idx_2 - 1]
            idx_2 += 1
            while idx_2 < len_A:
                if A[idx_2] - A[idx_2 - 1] != diff:
                    break
                idx_2 += 1
            num = idx_2 - idx_1
            if num > 2:
                num -= 2
                result += (1 + num) * num / 2
            idx_1 = idx_2 - 1

        return result
