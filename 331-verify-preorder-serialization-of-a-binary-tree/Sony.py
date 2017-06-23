class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        input_list = preorder.split(',')
        list_len = len(input_list)

        def dfs(index):
            if index >= list_len:
                return -1
            if input_list[index] == '#':
                return index
            index = dfs(index + 1)
            if -1 == index:
                return -1
            index = dfs(index + 1)
            return index

        final_index = dfs(0)
        return final_index != -1 and final_index == list_len -1


if __name__ == '__main__':

    sol = Solution()
    preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"

    print sol.isValidSerialization(preorder)