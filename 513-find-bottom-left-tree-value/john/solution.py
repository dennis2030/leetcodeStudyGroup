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
        todo = [(root, 0)]
        maxLevel = -1
        leftMost = None
        while todo:
            curr, level = todo.pop(0)
            if level > maxLevel:
                maxLevel = level
                leftMost = curr.val
            if curr.left:
                todo.append((curr.left, level + 1))
            if curr.right:
                todo.append((curr.right, level + 1))
        return leftMost
