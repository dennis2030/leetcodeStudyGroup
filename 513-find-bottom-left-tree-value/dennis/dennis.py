# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue
class Solution(object):    
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        left_most = None        
        q = Queue.Queue()
        q.put(root)
        
        while not q.empty():
            num_this_round = q.qsize()
            for i in xrange(num_this_round):
                node = q.get()
                if i == 0:
                    left_most = node
                if node.left != None:
                    q.put(node.left)
                if node.right != None:
                    q.put(node.right)
                    
        return left_most.val                    
