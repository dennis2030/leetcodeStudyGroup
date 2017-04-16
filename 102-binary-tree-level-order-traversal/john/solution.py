# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        result = []

        if root is None:
            return result

        todos = [(root, 0)]
        while todos:
            node, level = todos.pop(0)

            if len(result) < level + 1:
                result.append([])

            result[level].append(node.val)

            if node.left:
                todos.append((node.left, level + 1))
            if node.right:
                todos.append((node.right, level + 1))

        return result
