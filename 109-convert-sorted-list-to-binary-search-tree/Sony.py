# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def makeTree(arr, start, end):
            root = None
            middle = int((start + end) / 2)
            root = TreeNode(arr[middle])
            if middle != end:
                if middle != start:
                    root.left = makeTree(arr, start, middle -1)
                root.right = makeTree(arr, middle + 1, end)

            return root

        if head == None:
            return
        arr = []
        ptr = head
        while ptr is not None:
            arr.append(ptr.val)
            ptr = ptr.next


        return makeTree(arr, 0, len(arr) - 1)




if __name__ == '__main__':

    sol = Solution()
    head = None
    ptr = head
    for i in xrange(0, 0):
        node = ListNode(i)
        if head is None:
            ptr = head = node
        else:
            ptr.next = node
            ptr = node
    ptr = head
#    while ptr is not None:
#        print ptr.val
#        ptr = ptr.next

    print sol.sortedListToBST(head)