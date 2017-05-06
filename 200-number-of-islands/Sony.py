class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        world_map = list()
        map_height = len(grid)
        if map_height == 0:
            return 0
        map_width = len(grid[0])
        def mapTour(island_num, i, j):
            if i - 1 >= 0 and world_map[i - 1][j] == -1:
                world_map[i - 1][j] = island_num
                mapTour(island_num, i - 1, j)
            
            if i + 1 < map_height and world_map[i + 1][j] == -1:
                world_map[i + 1][j] = island_num
                mapTour(island_num, i + 1, j)
                
            if j - 1 >= 0 and world_map[i][j - 1] == -1:
                world_map[i][j - 1] = island_num
                mapTour(island_num, i, j -1)
            
            if j + 1 < map_width and world_map[i][j + 1] == -1:
                world_map[i][j + 1] = island_num
                mapTour(island_num, i, j + 1)

        island_num = 0
        for i in xrange(map_height):
            row = list()
            for j in xrange(map_width):
                row.append(int(grid[i][j]) * -1)
            world_map.append(row)
        for i in xrange(map_height):
            for j in xrange(map_width):
                if world_map[i][j] == -1:
                    island_num += 1
                    world_map[i][j] = island_num
                    mapTour(island_num, i, j)
        return island_num
    

if __name__ == '__main__':
    sol = Solution()
    grid = ["11000","11000","00100","00011"]
    print sol.numIslands(grid)
