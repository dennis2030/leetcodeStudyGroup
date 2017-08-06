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

        def traverse(root):
            left_BST = True
            left_min = root.val
            left_max = root.val
            right_BST = True
            right_min = root.val
            right_max = root.val

            if root.left != None:
                left_BST, left_min, left_max = traverse(root.left)
                if left_BST == False or left_max >= root.val:
                    return [False, left_min, left_max]

            if root.right != None:
                right_BST, right_min, right_max = traverse(root.right)
                if right_BST == False or right_min <= root.val:
                    return [False, right_min, right_max]

            return [True, left_min, right_max]

        if root == None:
            return True

        bst, min, max = traverse(root)

        return bst
