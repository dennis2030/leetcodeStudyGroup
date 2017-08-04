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
        import sys
        def dfs(root, min_val, max_val):
            if root.val <= min_val or root.val >= max_val:
                return False
            if root.left is not None:
                if root.val <= root.left.val:
                    return False
                if not dfs(root.left, min_val, root.val):
                    return False
            if root.right is not None:
                if root.val >= root.right.val:
                    return False
                if not dfs(root.right, root.val, max_val):
                    return False
            return True

        return dfs(root, -sys.maxint, sys.maxint) if root else True


if __name__ == '__main__':

    sol = Solution()

    print sol.isValidBST(None)