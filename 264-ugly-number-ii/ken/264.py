class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        import heapq

        seen = set()
        seen.add(1)
        heap = [1]
        i = 0
        ans = []

        while True:
            d = heapq.heappop(heap)
            a = d * 2
            b = d * 3
            c = d * 5

            if a not in seen:
                seen.add(a)
                heapq.heappush(heap, a)
            if b not in seen:
                seen.add(b)
                heapq.heappush(heap, b)
            if c not in seen:
                seen.add(c)
                heapq.heappush(heap, c)

            i += 1
            ans.append(d)

            if i == n:
                break

        return ans[n - 1]
