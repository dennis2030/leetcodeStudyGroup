class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []

        def recurse(currNum, currList):
            if len(currList) == k:
                if sum(currList) == n:
                    results.append(list(currList))
                return
            if currNum > 9:
                return
            recurse(currNum + 1, currList + [currNum])
            recurse(currNum + 1, currList)

        recurse(1, [])

        return results
