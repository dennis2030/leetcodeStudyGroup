class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        candidates = []
        for idx, prime in enumerate(primes):
            heapq.heappush(candidates, (prime, idx))

        indices = [0] * len(primes)
        uglies = [1]
        seen = set()
        while len(uglies) < n:
            ugly, idx = heapq.heappop(candidates)
            indices[idx] += 1
            if ugly not in seen:
                uglies.append(ugly)
                seen.add(ugly)
            newly = primes[idx] * uglies[indices[idx]]
            heapq.heappush(candidates, (newly, idx))
        return uglies[n - 1]
