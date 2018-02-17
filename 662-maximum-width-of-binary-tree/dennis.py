# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Queue import Queue
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        max_width = 1
        q = Queue()
        
        # the second element of tuple is the index of TreeNode, starting from 1
        q.put((root, 1))
                
        while q.qsize() != 0:
            qsize_this_run = q.qsize()
            l_idx = r_idx = 0            
            for i in xrange(qsize_this_run):
                tmp_tuple = q.get()
                node = tmp_tuple[0]
                idx = tmp_tuple[1]
                
                # leftmost element
                if i == 0:
                    l_idx = idx
                elif i == (qsize_this_run - 1):
                    r_idx = idx
                
                if node.left != None:
                    q.put((node.left, idx * 2))
                if node.right != None:
                    q.put((node.right, idx * 2 + 1))
                    
            if r_idx - l_idx + 1 > max_width:                
                max_width = r_idx - l_idx + 1
            
        return max_width
