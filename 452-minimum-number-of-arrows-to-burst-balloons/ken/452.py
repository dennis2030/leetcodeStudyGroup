class Solution(object):
	def findMinArrowShots(self, points):
		"""
		:type points: List[List[int]]
		:rtype: int
		"""

		cnt = 0
		points = sorted(points, key = lambda point: point[1])
		rightEdge = None

		for point in points:
			if rightEdge is None:
				rightEdge = point[1]
				cnt += 1
				continue

			if point[0] <= rightEdge:
				continue

			rightEdge = point[1]
			cnt += 1

		return cnt
