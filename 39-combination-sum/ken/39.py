class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ans = []
        dp = {}

        def sameList(a, b):
            a.sort()
            b.sort()

            return a == b

        def appendIfNot(l, e):
            for i in l:
                if sameList(i, e):
                    return
            l.append(e)

        def rec(target):
            if target in dp:
                return dp[target]

            ans = []
            for candidate in candidates:
                nextTarget = target - candidate
                if nextTarget == 0:
                    appendIfNot(ans, [candidate])
                elif nextTarget > 0:
                    subCombinations = rec(nextTarget)

                    if len(subCombinations) == 0:
                        continue

                    for subCombination in subCombinations:
                        cc = list(subCombination)
                        cc.append(candidate)
                        appendIfNot(ans, cc)

            if len(ans) > 0:
                dp[target] = ans

            return ans

        ans = rec(target)

        return ans
