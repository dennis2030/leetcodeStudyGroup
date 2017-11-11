class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        coords = [click]
        num_rows = len(board)
        if 0 == num_rows:
            return []
        num_cols = len(board[0])
        #print another_board
        
        while len(coords) > 0:
            coord = coords.pop()
            row = coord[0]
            col = coord[1]
            point = board[row][col]
            if point == 'E':
                num_bomb = 0
                neighbors = []
                for neighbor_row in xrange(row - 1, row + 2):
                    if neighbor_row < 0 or neighbor_row >= num_rows:
                        continue
                    for neighbor_col in xrange(col - 1, col + 2):
                        if neighbor_col < 0 or neighbor_col >= num_cols:
                            continue
                        if neighbor_row == row and neighbor_col == col:
                            continue
                        neighbor = board[neighbor_row][neighbor_col]
                        if neighbor == 'M':
                            num_bomb += 1
                        elif neighbor == 'E':
                            neighbors.append([neighbor_row, neighbor_col])
                if num_bomb == 0:
                    board[row][col] = 'B'
                    for neighbor in neighbors:
                            coords.append(neighbor)
                else:
                    board[row][col] = str(num_bomb)
            elif point == 'M':
                board[row][col] = 'X'
                break
                
        return board
