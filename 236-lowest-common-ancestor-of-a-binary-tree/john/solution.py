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
        def findPathInner(curr, target, path):
            if curr is None:
                return
            path.append(curr)

            found = False
            if curr is target:
                return True

            if findPathInner(curr.left, target, path):
                return True
            if findPathInner(curr.right, target, path):
                return True

            if not found:
                path.pop()

        def findPath(target):
            path = []
            findPathInner(root, target, path)
            return path

        def findLastCommon(pPath, qPath):
            assert pPath[0] is qPath[0]

            idx = 1
            while idx < len(pPath) and idx < len(qPath):
                if pPath[idx] is not qPath[idx]:
                    break
                idx += 1

            return pPath[idx - 1]

        pPath = findPath(p)
        qPath = findPath(q)

        ancestor = findLastCommon(pPath, qPath)

        return ancestor
