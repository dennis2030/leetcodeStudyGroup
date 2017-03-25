# Definition for a binary tree node.
# class TreeNode(object):
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None

class Solution(object):
	def generateTrees(self, n):
		"""
		:type n: int
		:rtype: List[TreeNode]
		"""
		def genTree(root, left, right):
			r = TreeNode(root.val)
			r.left = left
			r.right = right
			
			return r

		def recursive(start, end):
			if start > end:
				return [None]
			if start == end:
				node = TreeNode(start)
				return [node]

			res = []
			for i in xrange(start, end + 1):
				root = TreeNode(i)
				left_start = start
				left_end = i - 1
				right_start = i + 1
				right_end = end

				lefts = recursive(left_start, left_end)
				rights = recursive(right_start, right_end)

				for left in lefts:
					for right in rights:
						res.append(genTree(root, left, right))

			return res
			
		return recursive(1, n)
