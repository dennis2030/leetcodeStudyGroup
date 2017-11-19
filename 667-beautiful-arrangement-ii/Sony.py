class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = range(n, k, -1)
        diff = k
        op_minus = True
        val = 1 + k
        while k > 0:
            if op_minus:
                val = val - k
            else:
                val = val + k
            result.append(val)
            op_minus = not op_minus
            k -= 1

        return result
