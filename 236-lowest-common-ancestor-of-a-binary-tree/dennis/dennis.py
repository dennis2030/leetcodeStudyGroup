# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):    
    def hasPorQ(self, node, p, q):
        if (node == None) or (node == p) or (node == q):
            return node
        
        left = self.hasPorQ(node.left, p, q)
        right = self.hasPorQ(node.right, p, q)
        
        if left and right:
            return node
        if left == None:
            return right
        if right == None:
            return left
        return node
        
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        return self.hasPorQ(root, p, q)
        
