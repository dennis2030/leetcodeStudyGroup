# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def countNumNodes(head):
            n = 0
            curr = head
            while curr is not None:
                curr = curr.next
                n += 1
            return n

        def advance(head, count):
            curr = head
            for i in range(count):
                curr = curr.next
            return curr

        def makeBst(head, n):
            print 'n', n
            if n == 0:
                return None
            if n == 1:
                return TreeNode(head.val)

            middle = n / 2
            prev = advance(head, middle - 1)
            target = prev.next
            prev.next = None

            root = TreeNode(target.val)
            root.left = makeBst(head, middle)
            root.right = makeBst(target.next, n - middle - 1)

            return root

        n = countNumNodes(head)
        return makeBst(head, n)
