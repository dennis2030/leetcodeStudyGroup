# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def genBST(self, root, left, right):
        node = TreeNode(root)
        node.left = left
        node.right = right
        return node
    def recursiveGenBST(self, start, end):
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(start)]

        bst_list = []
        # Select i as root
        for i in xrange(start, end + 1):
            left_options = self.recursiveGenBST(start, i - 1)
            right_options = self.recursiveGenBST(i + 1, end)

            combinations = [self.genBST(i, left, right) for left in left_options for right in right_options]
            bst_list += combinations

        return bst_list

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.recursiveGenBST(1, n)
