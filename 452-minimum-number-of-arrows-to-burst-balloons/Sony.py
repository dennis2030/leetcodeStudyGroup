class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        end_sorted_list = []
        for point in points:
            end_sorted_list.append(point)
        list_len = len(points)

        end_sorted_list.sort(key = lambda point: point[1])
        cur_end = None
        end_list_idx = 0
        num_arrow = 0

        while end_list_idx < list_len:
            cur_point = end_sorted_list[end_list_idx]
            end_list_idx += 1
            if cur_point[0] < cur_end:
                continue
            num_arrow += 1
            cur_end = cur_point[1]
        return num_arrow


if __name__ == '__main__':

    sol = Solution()
    points = [[10,16], [2,8], [1,6], [7,12]]
    #points = [[1,2],[3,4],[5,6],[7,8]]
    print sol.findMinArrowShots(points)