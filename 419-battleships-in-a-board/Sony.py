class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        board_height = len(board)
       	board_width = len(board[0]) if board_height > 0 else 0
       	num = 0
       	i = j = 0
       	print board_height, board_width
       	while i < board_height:
       		print 'i is', i
       		while j < board_width:
       			if board[i][j] == 'X':
       				print i, j
       				if i == 0 or board[i-1][j] != 'X':
       					num += 1
       				j = j + 1
       				while j < board_width and board[i][j] == 'X':
       					j += 1
       			else:
       				j += 1
       		i += 1
       		j = 0
       	return num



if __name__ == '__main__':

    sol = Solution()
    board = ["X..X", "...X", "...X"]

    print sol.countBattleships(board)