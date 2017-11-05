class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        wall_height = len(wall)
        if wall_height == 0:
            return 0

        wall_width = len(wall[0])
        if wall_width == 0:
            return 0

        edge_dict = dict()
        for column in wall:
            edge = 0
            for i in xrange(len(column) - 1):
                edge += column[i]
                if edge in edge_dict:
                    edge_dict[edge] += 1
                else:
                    edge_dict[edge] = 1

        most_edge = 0
        for edge, count in edge_dict.items():
            most_edge = max(most_edge, count)

        return wall_height - most_edge

if __name__ == '__main__':

    sol = Solution()
    wall = [[1,2,2,1],
            [3,1,2],
            [1,3,2],
            [2,4],
            [3,1,2],
            [1,3,1,1]]
    print sol.leastBricks(wall)