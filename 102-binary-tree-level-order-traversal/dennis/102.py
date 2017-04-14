# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        q = Queue.Queue()
        if None != root:
            q.put(root)

        final_ans = []

        while not q.empty():
            num_of_node_this_round = q.qsize()
            item_this_round = []
            for i in xrange(num_of_node_this_round):
                node = q.get()
                item_this_round.append(node.val)
                if None != node.left:
                    q.put(node.left)
                if None != node.right:
                    q.put(node.right)
            final_ans.append(item_this_round)

        return final_ans
