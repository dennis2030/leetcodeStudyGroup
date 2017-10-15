# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def _buildTree(preorder_start, inorder_start, tree_size):
            if tree_size == 0:
                return None
            print preorder_start, inorder_start, tree_size
            root = TreeNode(preorder[preorder_start])
            idx = inorder.index(preorder[preorder_start])
            left_tree_size = idx - inorder_start
            root.left = _buildTree(preorder_start + 1, inorder_start, left_tree_size)
            root.right = _buildTree(preorder_start + 1 + left_tree_size, idx + 1, tree_size - left_tree_size - 1)
            return root
        return _buildTree(0, 0, len(preorder))

if __name__ == '__main__':

    sol = Solution()
    preorder = [1, 2]
    inorder = [2, 1]
    print sol.buildTree(preorder, inorder)