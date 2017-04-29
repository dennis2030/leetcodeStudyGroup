class Solution(object):
    def BFSsearch(self, grid, row, col, idx):
        grid[row][col] = str(idx)
        # top
        if row > 0 and grid[row-1][col] == '1':
            self.BFSsearch(grid, row - 1, col, idx)
        # bottom
        if row + 1 < len(grid) and grid[row + 1][col] == '1':
            self.BFSsearch(grid, row + 1, col, idx)
        # left
        if col > 0 and grid[row][col - 1] == '1':
            self.BFSsearch(grid, row, col - 1, idx)
        # right
        if col + 1 < len(grid[row]) and grid[row][col+ 1] == '1':
            self.BFSsearch(grid, row, col + 1, idx)
            
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        idx = 2
        
        for row in xrange(len(grid)):
            for col in xrange(len(grid[row])):
                if grid[row][col] == '1':
                    self.BFSsearch(grid, row, col, idx)
                    idx += 1
                    
        return idx - 2
