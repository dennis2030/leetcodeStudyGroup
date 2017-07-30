# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.real_flatten(root)

    def real_flatten(self, root):
        if root.left == None:
            if root.right == None:
                return root
            else:
                return self.real_flatten(root.right)
        else:
            concate_node = self.real_flatten(root.left)
            if root.right != None:
                new_concate_node = self.real_flatten(root.right)
                concate_node.right = root.right
            else:
                new_concate_node = concate_node
            root.right = root.left
            root.left = None
            return new_concate_node

if __name__ == '__main__':

    sol = Solution()
    print sol.flatten(None)