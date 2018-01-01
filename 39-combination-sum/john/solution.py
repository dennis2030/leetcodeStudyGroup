class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []

        def recurse(curr, idx):
            currSum = sum(curr)

            if currSum > target:
                return
            elif currSum == target:
                results.append(list(curr))
                return

            for jdx, candidate in enumerate(candidates):
                if jdx < idx:
                    continue
                curr.append(candidate)
                recurse(curr, jdx)
                curr.pop()

        recurse([], 0)

        return results
