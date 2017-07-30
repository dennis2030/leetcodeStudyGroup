# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def concatList(src, dst):
            curr = src
            while curr.right != None:
                curr = curr.right
            curr.right = dst

        def flattenInner(node):
            if node.left:
                flattenInner(node.left)
            if node.right:
                flattenInner(node.right)

            if node.left:
                if node.right:
                    concatList(node.left, node.right)
                node.right = node.left
                node.left = None

        if root is None:
            return

        flattenInner(root)
