# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global max_depth, b_l_value
        if root == None:
            return None

        max_depth = -1
        b_l_value = None

        def dfs(node, depth):
            global max_depth, b_l_value
            if node.left != None:
                dfs(node.left, depth + 1)
            if node.right != None:
                dfs(node.right, depth + 1)
            if depth > max_depth:
                max_depth = depth
                b_l_value = node.val
        dfs(root, 0)
        return b_l_value


if __name__ == '__main__':

    sol = Solution()

    print sol.findBottomLeftValue(None)