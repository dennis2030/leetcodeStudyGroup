# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(node, p, q):
            family = set((node,))

            if node.left is not None:
                left_lca, left_set = dfs(node.left, p, q)
                if left_lca is not None:
                    return left_lca, None
                family = family.union(left_set)

            if node.right is not None:
                right_lca, right_set = dfs(node.right, p, q)
                if right_lca is not None:
                    return right_lca, None
                family = family.union(right_set)

            if p in family and q in family:
                return node, None
            else:
                return None, family

        return dfs(root, p, q)[0]



if __name__ == '__main__':

    sol = Solution()

    print sol.lowestCommonAncestor(root, p, q):