# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isFound(self):
        return self.cnt == self.k

    def rec(self, root):
        if root.left != None:
            val = self.rec(root.left)
            if self.isFound():
                return val

        self.cnt += 1
        if self.isFound():
            return root.val

        if root.right != None:
            val = self.rec(root.right)
            if self.isFound():
                return val

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        self.cnt = 0
        self.k = k

        return self.rec(root)