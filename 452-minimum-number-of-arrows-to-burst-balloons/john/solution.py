class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ranges = []

        def calcIntersect(point1, point2):
            if point1[1] < point2[0] or point1[0] > point2[1]:
                return None
            left = max(point1[0], point2[0])
            right = min(point1[1], point2[1])
            return [left, right]

        def findRange(point):
            if not ranges:
                return None
            range_ = ranges[-1]
            if calcIntersect(range_['arrow'], point) is None:
                return None
            return range_

        points.sort()
        for point in points:
            range_ = findRange(point)

            if range_ is None:
                ranges.append({
                    'arrow': point,
                    'ballons': [point]
                })
            else:
                range_['arrow'] = calcIntersect(range_['arrow'], point)
                range_['ballons'].append(point)

        return len(ranges)
