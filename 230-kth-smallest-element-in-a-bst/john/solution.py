# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        curr = {
            'idx': 0,
        }

        def dfs(node):
            if node.left:
                num = dfs(node.left)
                if num is not None:
                    return num

            curr['idx'] += 1
            if curr['idx'] == k:
                return node.val

            if node.right:
                num = dfs(node.right)
                if num is not None:
                    return num

            return None

        return dfs(root)
