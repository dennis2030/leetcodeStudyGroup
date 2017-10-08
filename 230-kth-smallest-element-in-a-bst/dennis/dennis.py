# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inOrderTraverse(self, node, k):
        if node == None or self.ans != None:
            return
        self.inOrderTraverse(node.left, k)
        self.count += 1
        if self.count == k:
            self.ans = node.val
            return
        self.inOrderTraverse(node.right, k)
        
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.ans = None
        self.inOrderTraverse(root, k)
        return self.ans
        
