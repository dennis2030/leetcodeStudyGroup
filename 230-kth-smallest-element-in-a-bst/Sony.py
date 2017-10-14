# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def in_order_dfs(root, i):
            result = None
            if root.left != None:
                i, result = in_order_dfs(root.left, i)
                if i == k:
                    return i, result
            i += 1
            if i == k:
                return k, root.val

            if root.right != None:
                i, result = in_order_dfs(root.right, i)
            print 'right', i, result
            return i, result

        return in_order_dfs(root, 0)[1] if root else None


if __name__ == '__main__':

    sol = Solution()

    print sol.kthSmallest(None, 20)