class Solution(object):
    def findMaxForm(self, strs, m, n):
        from operator import attrgetter
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        m_1 = m + 1
        n_1 = n + 1
        dp_map = [[0  for j in xrange(m_1)] for i in xrange(n_1)]
        for one_str in strs:
            zero_num = one_str.count('0')
            one_num = len(one_str) - zero_num
            for i in xrange(n_1 - one_num):
                for j in xrange(m_1 - zero_num):
                    dp_map[i][j] = max(dp_map[i + one_num][j + zero_num] + 1, dp_map[i][j])
        return max(max(one_line) for one_line in dp_map)
