class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a_len = len(A)

        weighted_sum = 0
        total = 0
        max_value  = 0
        for idx, value in enumerate(A):
            weighted_sum = weighted_sum + idx * value
            total = total + value

        max_value = weighted_sum
        pivot = a_len - 1

        while pivot > 0:
            weighted_sum = weighted_sum + total - a_len * A[pivot]
            pivot = pivot - 1
            max_value = max(max_value, weighted_sum)

        return max_value

if __name__ == '__main__':
    sol = Solution()

    A = [4, 3, 2, 6]


    print sol.maxRotateFunction(A)