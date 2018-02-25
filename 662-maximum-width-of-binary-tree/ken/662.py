# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        cur = [(root, 0)]
        ans = 0
        while cur:
            next = []
            left = -1
            right = -1

            for i in xrange(len(cur)):
                node = cur[i][0]
                pos = cur[i][1]

                if node is None:
                    continue

                if left == -1:
                    left = pos

                right = pos
                next.append((node.left, pos * 2))
                next.append((node.right, pos * 2 + 1))

            ans = max(ans, right - left + 1)
            cur = next

        return ans
