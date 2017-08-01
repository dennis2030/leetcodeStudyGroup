# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    prev = None
    #def isValid(self, idx):
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        if not self.isValidBST(root.left):
            return False
        
        if self.prev != None and root.val <= self.prev:
            return False
        
        self.prev = root.val
        
        if not self.isValidBST(root.right):
            return False
        
        return True
        
