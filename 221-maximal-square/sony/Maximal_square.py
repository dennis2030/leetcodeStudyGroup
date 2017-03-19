class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        height = len(matrix)
        if height == 0:
            return 0
        width = len(matrix[0])
        dp_matrix = list()

        dp_matrix.append(list())
        for i in xrange(width):
            dp_matrix[0].append(int(matrix[0][i]))
        maximal_len = max(dp_matrix[0])

        for i in xrange(1, height):
            dp_matrix.append(list())
            dp_matrix[i].append(int(matrix[i][0]))
            round_max_len = dp_matrix[i][0]
            for j in xrange(1, width):
                if matrix[i][j] == '0':
                    dp_matrix[i].append(0)
                else:
                    if dp_matrix[i - 1][j] == 0 or dp_matrix[i][j - 1] == 0:
                        dp_matrix[i].append(1)
                    elif dp_matrix[i - 1][j] == dp_matrix[i][j - 1]:
                        value = dp_matrix[i - 1][j]
                        if dp_matrix[i - value][j - value] > 0:
                            value += 1
                        dp_matrix[i].append(value)
                    else:
                        dp_matrix[i].append(min(dp_matrix[i - 1][j], dp_matrix[i][j - 1]) + 1)
                    round_max_len = max(round_max_len, dp_matrix[i][j])
            maximal_len = max(maximal_len, round_max_len)

        return maximal_len * maximal_len

if __name__ == '__main__':
    sol = Solution()
    matrix = [  "10100",
                "11111",
                "11111",
                "10010"]

    print sol.maximalSquare(matrix)