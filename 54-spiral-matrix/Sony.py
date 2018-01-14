class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        go_height = len(matrix)
        if go_height == 0:
            return []
        go_width =  len(matrix[0])
        go_height -= 1
        
        dir_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x_idx = 0
        y_idx = 0
        dir_idx = 0
        go_idx = 0
        result_list = list()
        go_length = go_width
        
        while go_length != 0:
            result_list.append(matrix[y_idx][x_idx])
            go_idx += 1
            if go_idx == go_length:
                dir_idx = (dir_idx + 1) % 4
                go_idx = 0
                if dir_idx % 2 == 1:
                    go_width -= 1
                    go_length = go_height
                else:
                    go_height -= 1
                    go_length = go_width
            y_idx += dir_list[dir_idx][0]
            x_idx += dir_list[dir_idx][1]
        return result_list
