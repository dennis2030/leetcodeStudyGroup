class Solution(object):
	def numIslands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""

		class Param(object):
			def __init__(self, grid, visited, col_num, row_num):
				self.grid = grid
				self.visited = visited
				self.col_num = col_num
				self.row_num = row_num

		def in_boundary(param, i, j):
			if i >= 0 and j >= 0 and i < param.row_num and j < param.col_num:
				return True
			return False

		def should_visit(param, i, j):
			if in_boundary(param, i, j) and param.grid[i][j] == "1" and param.visited[i][j] == False:
				return True
			return False

		if len(grid) == 0:
			return 0

		n = 0
		visited = []
		col_num = len(grid[0])
		row_num = len(grid)
		param = Param(grid, visited, col_num, row_num)

		for i in xrange(len(grid)):
			visited.append([])
			for j in xrange(len(grid[i])):
				visited[i].append(False)

		def visit(param, i, j):
			if should_visit(param, i, j) == False:
				return

			visited[i][j] = True

			visit(param, i + 1, j)
			visit(param, i, j + 1)
			visit(param, i - 1, j)
			visit(param, i, j - 1)

		for i in xrange(len(grid)):
			for j in xrange(len(grid[0])):
				if should_visit(param, i, j):
					n += 1
					visit(param, i, j)

		return n
