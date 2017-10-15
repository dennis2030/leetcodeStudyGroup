# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.result = list()
        self.stack = list()
        self.cur_sum = 0
    def pathSum(self, root, target_sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(root):
            if root is None:
                return
            if root.left == None and root.right == None:
                if root.val + self.cur_sum == target_sum:
                    candi_list = list(self.stack)
                    candi_list.append(root.val)
                    self.result.append(candi_list)
                return

            self.stack.append(root.val)
            self.cur_sum += root.val
            dfs(root.left)
            dfs(root.right)
            self.stack.pop()
            self.cur_sum -= root.val
        dfs(root)
        return self.result

if __name__ == '__main__':

    sol = Solution()
    print sol.pathSum(None, 0)