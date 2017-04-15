# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution(object):
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""

		if root is None:
			return []

		result = []
		curResult = []
		curList = [root]
		nextList = []

		while len(curList) > 0:
			for cur in curList:
				curResult.append(cur.val)
				if cur.left is not None:
					nextList.append(cur.left)
				if cur.right is not None:
					nextList.append(cur.right)

			result.append(curResult)
			curResult = []
			curList = nextList
			nextList = []

		return result
