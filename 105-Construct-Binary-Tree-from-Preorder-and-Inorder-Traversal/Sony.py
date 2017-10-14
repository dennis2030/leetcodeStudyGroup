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
        if len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        print idx
        root.left = self.buildTree(preorder[1:idx + 1], inorder[0:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return root

if __name__ == '__main__':

    sol = Solution()
    preorder = [1, 2]
    inorder = [2, 1]
    print sol.buildTree(preorder, inorder)