class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        import heapq
        primes_num = len(primes)
        prime_idx_dict = dict()
        candidate_heap = []
        for prime in primes:
            prime_idx_dict[prime] = 0
            heapq.heappush(candidate_heap, (prime, prime))
        super_ugly_number_list = [1]

        i = 1
        candidate = heapq.heappop(candidate_heap)
        last_num =1
        while i < n:
            prime = candidate[1]
            if candidate[0] != last_num:
                last_num = candidate[0]
                super_ugly_number_list.append(last_num)
                i += 1

            candidate = heapq.heappushpop(candidate_heap, (prime * super_ugly_number_list[prime_idx_dict[prime]], prime))
            prime_idx_dict[prime] += 1
        return super_ugly_number_list[n - 1]


if __name__ == '__main__':

    sol = Solution()
    n = 12
    primes = [2, 7, 13, 19]
    print sol.nthSuperUglyNumber(n, primes)