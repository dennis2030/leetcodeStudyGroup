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

        def flattenChild(root):
            listEnd = root
            leftEnd = None

            if root.left != None:
                leftEnd = flattenChild(root.left)
                listEnd = leftEnd

            if root.right != None:
                listEnd = flattenChild(root.right)

            if root.left != None:
                leftEnd.right = root.right
                root.right = root.left
                root.left = None

            return listEnd

        if root == None:
            return

        flattenChild(root)
