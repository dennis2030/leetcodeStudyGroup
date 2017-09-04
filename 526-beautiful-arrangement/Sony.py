class Solution(object):
    def __init__(self):
        self.cache = {}

    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def assignBeauty(candidates, index, remaining_num):
            total  = 0
            if index == N:
                for num in remaining_num:
                    if N % num == 0:
                        total += 1
            else:
                i = 0
                while i < len(remaining_num):
                    if remaining_num[i] in candidates[index]:
                        new_remaining_nums = remaining_num[:i] + remaining_num[i + 1:]
                        if (i, remaining_num) not in self.cache:
                            sub_num = assignBeauty(candidates, index + 1, new_remaining_nums)
                            self.cache[(i, remaining_num)] = sub_num
                        else:
                            sub_num = self.cache[(i, remaining_num)]
                        total += sub_num
                    i += 1
            return total

        candidates = [[i] for i in xrange(N + 1)]
        for i in xrange(1, N + 1):
            for j in xrange(i * 2, N + 1, i):
                candidates[i].append(j)
                candidates[j].append(i)

        return assignBeauty(candidates, 1, tuple(range(1, N + 1)))

if __name__ == '__main__':

    sol = Solution()

    N = 10
    print sol.countArrangement(N)