# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        current = []

        def rec(root):
            current.append(root.val)

            if root.left is None and root.right is None:
                if sum(current) == sum:
                    ans.append(list(current))
            elif root.left:
                rec(root.left)
            elif root.right:
                rec(root.right)

            current.pop()

        return ans
