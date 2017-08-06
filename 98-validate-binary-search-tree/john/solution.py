# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is not None:
            rightMost = root.left
            while rightMost.right is not None:
                rightMost = rightMost.right
            if rightMost.val >= root.val:
                return False
        if root.right is not None:
            leftMost = root.right
            while leftMost.left is not None:
                leftMost = leftMost.left
            if leftMost.val <= root.val:
                return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)
