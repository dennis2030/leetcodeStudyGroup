# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        num = preorder[0]
        idx = inorder.index(num)
        leftInorder = inorder[:idx]
        rightInorder = inorder[idx + 1:]
        leftPreorder = preorder[1:len(leftInorder) + 1]
        rightPreorder = preorder[len(leftInorder) + 1:]

        root = TreeNode(num)
        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)

        return root
