# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cur = [root]
        left = root.val

        while len(cur):
            next = []
            left = cur[0].val
            for node in cur:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)

            cur = next

        return left
