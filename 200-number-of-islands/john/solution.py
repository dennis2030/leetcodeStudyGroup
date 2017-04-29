class Solution(object):
    def paintZero(self, grid, r, c):
        if grid[r][c] == '0':
            return

        grid[r][c] = '0'

        if r > 0:
            self.paintZero(grid, r - 1, c)
        if r < len(grid) - 1:
            self.paintZero(grid, r + 1, c)
        if c > 0:
            self.paintZero(grid, r, c - 1)
        if c < len(grid[r]) - 1:
            self.paintZero(grid, r, c + 1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    self.paintZero(grid, r, c)
                    count += 1

        return count
