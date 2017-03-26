# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def generateTrees(self, n):
		"""
		:type n: int
		:rtype: List[TreeNode]
		"""
		if n == 0:
			return None
		return self.genSubTree(1, n)

	def genSubTree(self, start, end):
		result_list = list()

		if start < end:
			for i in xrange(start, end + 1):
				left_subtrees = self.genSubTree(start, i - 1)
				right_subtrees = self.genSubTree(i + 1, end)

				#pcombination with left_subtrees and right_subtrees
				for left_subtree in left_subtrees:
					for right_subtree in right_subtrees:
						new_node = TreeNode(i)
						new_node.left = left_subtree
						new_node.right = right_subtree
						result_list.append(new_node)
		elif start > end:
			result_list.append(None)
		else:
			new_node = TreeNode(start)
			result_list.append(new_node)

		return result_list

if __name__ == '__main__':
    sol = Solution()

    sol.generateTrees(0)