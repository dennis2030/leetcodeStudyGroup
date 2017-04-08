# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def bfs(result_list, current_level_queue):
            next_level_queue = list()
            current_level_list = list()
            for item in current_level_queue:
                current_level_list.append(item.val)
                if item.left != None:
                    next_level_queue.append(item.left)
                if item.right != None:
                    next_level_queue.append(item.right)

            result_list.append(current_level_list)
            if len(next_level_queue) > 0:
                bfs(result_list, next_level_queue)

        result_list = list()
        if root == None:
            return result_list
        bfs(result_list, [root])
        return result_list


if __name__ == '__main__':
    sol = Solution()

    print sol.levelOrder()