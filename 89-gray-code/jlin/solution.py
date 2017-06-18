class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        codes = ['']

        for i in range(n):
            news = []
            for code in codes:
                news.append('0' + code)
            for code in reversed(codes):
                news.append('1' + code)
            codes = news

        nums = [int(code, 2) for code in codes]

        return nums
