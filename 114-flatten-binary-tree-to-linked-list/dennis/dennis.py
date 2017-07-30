# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find_tail(self, node):
        if node == None:
            return None
        if node.right == None:
            return node
        return self.find_tail(node.right)
    
    def recursive(self, node):        
        if node == None:
            return None
        tmp_right = self.recursive(node.right) if node.right != None else None                
        tmp_left = self.recursive(node.left) if node.left != None else None
        
        tmp_left_tail = self.find_tail(tmp_left)
        
        left_tail = tmp_left_tail if tmp_left_tail != None else node
        
        node.right = tmp_left        
        left_tail.right = tmp_right
        
        node.left = None
        return node
        
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.recursive(root)
        
        
