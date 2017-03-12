class Solution(object):
	def computeArea(self, A, B, C, D, E, F, G, H):
		"""
		:type A: int
		:type B: int
		:type C: int
		:type D: int
		:type E: int
		:type F: int
		:type G: int
		:type H: int
		:rtype: int
		"""

		def HasIntersect(rect1, rect2):
			x1 = max(rect1[0], rect2[0])
			y1 = max(rect1[1], rect2[1])
			x2 = min(rect1[2], rect2[2])
			y2 = min(rect1[3], rect2[3])

			if x1 < x2 and y1 < y2:
				return True, (x1, y1, x2, y2)
			else:
				return False, None

		def RectArea(rect):
			area = (rect[2] - rect[0]) * (rect[3] - rect[1])

			return area

		rect1 = (A, B, C, D)
		rect2 = (E, F, G, H)

		area = RectArea(rect1) + RectArea(rect2)

		valid, intectRect = HasIntersect(rect1, rect2)

		if valid:
			area -= RectArea(intectRect)

		return area