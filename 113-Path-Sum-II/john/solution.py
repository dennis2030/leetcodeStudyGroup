# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        results = []

        def dfs(node, stack, accum):
            if node is None:
                return

            stack.append(node)
            accum += node.val

            if node.left is None and node.right is None:
                if accum == target:
                    results.append([node.val for node in stack])
            else:
                dfs(node.left, stack, accum)
                dfs(node.right, stack, accum)

            stack.pop()
            accum -= node.val

        dfs(root, [], 0)

        return results
