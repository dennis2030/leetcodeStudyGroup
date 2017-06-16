class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result_list = []
        global num
        num = 0

        def dfs(level):
            global num
            if level == 0:
                result_list.append(num)
                num ^= 0x01
                result_list.append(num)
            else:
                dfs(level - 1)
                num ^= 0x1 << level
                dfs(level - 1)
        if n > 0:
            dfs(n - 1)
        else:
            result_list.append(0)
        return result_list



if __name__ == '__main__':

    sol = Solution()

    n = 2
    print sol.grayCode(n)