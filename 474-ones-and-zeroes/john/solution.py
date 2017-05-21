class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        items = []
        for s in strs:
            bits = [int(digit) for digit in s]
            items.append({
                'num0s': len(bits) - sum(bits),
                'num1s': sum(bits),
            })

        cache = {}

        def recurse(total, m, n):
            if total == 0:
                return 0

            key = (total, m, n)

            if key in cache:
                return cache.pop(key)

            item = items[total - 1]

            dontPick = recurse(total - 1, m, n)
            if m < item['num0s'] or n < item['num1s']:
                cache[key] = dontPick
            else:
                doPick = 1 + recurse(total - 1, m - item['num0s'], n - item['num1s'])
                cache[key] = max(dontPick, doPick)

            return cache[key]

        return recurse(len(items), m, n)
