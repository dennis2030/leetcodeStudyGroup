# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def dfs(root, p, q):
            rootMatch = 1 if (root == p or root == q) else 0

            if (root == None) or \
               (root.left == None and root.right == None):
                return [rootMatch, None]

            left = dfs(root.left, p, q)
            if left[0] == 2:
                return left

            right = dfs(root.right, p, q)
            if right[0] == 2:
                return right

            totalFound = rootMatch + left[0] + right[0]
            node = root if (totalFound == 2) else None

            return [totalFound, node]

        result = dfs(root, p, q)
        return result[1]
