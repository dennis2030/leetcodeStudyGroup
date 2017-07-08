class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        class Point:
            def __init__(self, start, end):
                self.start = start
                self.end = end
                self.visited = False

        start_sorted_list = []
        for _point in points:
            start_sorted_list.append(Point(_point[0], _point[1]))
        end_sorted_list = list(start_sorted_list)
        list_len = len(points)

        start_sorted_list.sort(key = lambda point: point.start)
        end_sorted_list.sort(key = lambda point: point.end)

        start_list_idx = end_list_idx = 0
        num_arrow = 0

        while end_list_idx < list_len:
            cur_point = end_sorted_list[end_list_idx]
            if cur_point.visited:
                end_list_idx += 1
                continue

            num_arrow += 1
            cur_point.visited = True
            while start_list_idx < list_len:
                another_point = start_sorted_list[start_list_idx]
                if another_point.start > cur_point.end:
                    break
                another_point.visited = True
                start_list_idx += 1

            if start_list_idx >= list_len:
                break
            end_list_idx += 1
        return num_arrow


if __name__ == '__main__':

    sol = Solution()
    points = [[10,16], [2,8], [1,6], [7,12]]
    # points = [[1,2],[3,4],[5,6],[7,8]]
    print sol.findMinArrowShots(points)