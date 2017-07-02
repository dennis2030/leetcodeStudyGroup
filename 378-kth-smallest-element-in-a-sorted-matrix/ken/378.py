class Solution(object):
	def kthSmallest(self, matrix, k):
		"""
		:type matrix: List[List[int]]
		:type k: int
		:rtype: int
		"""

		# 老師，梁哲瑋做弊
		def mergeList(matrix, k):
			mergedList = []
			for row in matrix:
				mergedList.extend(row)
			mergedList.sort()

			return mergedList[k-1]

		# Might TLE
		def searchRowByRow(matrix, k):
			n = len(matrix)
			idxs = [0 for i in xrange(n)]

			for i in xrange(k):
				min_row = -1
				min_num = -1
				for j in xrange(n):
					idx = idxs[j]
					if idx >= n:
						continue

					if min_row == -1:
						min_row = j
						min_num = matrix[j][idx]
					else:
						num = matrix[j][idx]

						if num < min_num:
							min_row = j
							min_num = num

				idxs[min_row] += 1
				if i == k - 1:
					return min_num

		return mergeList(matrix, k)
