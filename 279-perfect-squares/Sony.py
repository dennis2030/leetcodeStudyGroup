class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        import math
        k = int(math.sqrt(n))
        candidates = [x * x for x in xrange(k, 0, -1)]
        min_num = n
        num_map = {0: 0}
        for x in xrange(k, 0, -1):
            num = x * x
            candidates.append(num)
            num_map[num] = 1
        if n in num_map:
            return 1
        def find_min_num(candidate_idx, remaining, depth):
            if remaining in num_map:
                return num_map[remaining]
            if depth >= min_num:
                num_map[remaining] = min_num + 1
                return min_num + 1
            cur_n = remaining
            for idx in xrange(candidate_idx, k):
                diff = remaining - candidates[idx]
                if diff < 0:
                    continue
                cur_n = min(cur_n, 1 + find_min_num(idx, diff, depth + 1))
            return cur_n
        for idx in xrange(k):
            diff = n - candidates[idx]
            if diff < 0:
                continue
            cur_n = min(n, 1 + find_min_num(idx, diff, 1))
            min_num = min(min_num, cur_n)

        return min_num



if __name__ == '__main__':

    sol = Solution()
    n = 13
    print sol.numSquares(n)