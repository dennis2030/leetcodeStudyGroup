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
        if root is None:
            return 0
        bfs_list = [(0, root)]
        max_width = 1
        while len(bfs_list) > 0:
            new_bfs_list = []
            for idx, node in bfs_list:
                if node.left is not None:
                    new_bfs_list.append((2 * idx, node.left))
                if node.right is not None:
                    new_bfs_list.append((2 * idx + 1, node.right))
            max_width = max(max_width, bfs_list[-1][0] - bfs_list[0][0] + 1)
            bfs_list = new_bfs_list
        return max_width
