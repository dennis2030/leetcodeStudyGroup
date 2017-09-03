class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        result = {
            'count': 0
        }

        candidatesList = []
        candidatesList.append(None)
        for idx in range(1, N + 1):
            candidates = []
            for num in range(1, N + 1):
                if idx % num == 0 or num % idx == 0:
                    candidates.append(num)
            candidatesList.append(candidates)

        def recurse(currList, used):
            if len(currList) == N:
                result['count'] += 1
                return

            currIdx = len(currList) + 1
            for num in candidatesList[currIdx]:
                if used[num]:
                    continue

                currList.append(num)
                used[num] = True

                recurse(currList, used)

                used[num] = False
                currList.pop()

        recurse([], [False] * (N + 1))

        return result['count']
