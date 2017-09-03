class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        def assignBeauty(candidates, total, index, remaining_num):
            #print total, index, remaining_num
            if index == N:
                for num in remaining_num:
                    if num in candidates[index]:
                        total += 1
            else:
                i = 0
                while i < len(remaining_num):
                    if remaining_num[i] not in candidates[index]:
                        i += 1
                        continue
                    used_num = remaining_num
                    total = assignBeauty(candidates, total, index + 1, remaining_num[:i] + remaining_num[i + 1:])
                    i += 1
            return total

        candidates = [[i] for i in xrange(N + 1)]
        for i in xrange(1, N + 1):

            for j in xrange(i * 2, N + 1, i):
                candidates[i].append(j)
                candidates[j].append(i)
        #print candidates

        return assignBeauty(candidates, 0, 1, [i for i in xrange(1, N + 1)])




if __name__ == '__main__':

    sol = Solution()

    N = 7
    print sol.countArrangement(N)