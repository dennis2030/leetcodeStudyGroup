class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)

        calculated = {}
        def recurse(curr):
            val = triangle[curr[0]][curr[1]]
            if curr[0] == n - 1:
                calculated[curr] = val
                return

            left = (curr[0] + 1, curr[1])
            right = (curr[0] + 1, curr[1] + 1)

            if left not in calculated:
                recurse(left)
            if right not in calculated:
                recurse(right)

            calculated[curr] = val + min(calculated[left], calculated[right])

        recurse((0, 0))

        return calculated[(0, 0)]
