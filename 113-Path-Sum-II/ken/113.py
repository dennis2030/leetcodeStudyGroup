# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        current = []

        def rec(root):
            if root is None:
                return

            current.append(root.val)

            if root.left is None and root.right is None:
                if sum(current) == target:
                    ans.append(list(current))

            rec(root.left)
            rec(root.right)

            current.pop()

        rec(root)

        return ans
