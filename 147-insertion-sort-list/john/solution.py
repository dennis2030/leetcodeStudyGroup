# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def insertBefore(self, new, old):
        new.val, old.val = old.val, new.val
        new.next = old.next
        old.next = new

    def insertPosition(self, todoNode, sortedHead):
        currNode = sortedHead
        tailNode = sortedHead
        while currNode:
            if currNode.val > todoNode.val:
                self.insertBefore(todoNode, currNode)
                return
            tailNode = currNode
            currNode = currNode.next

        tailNode.next = todoNode
        todoNode.next = None

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        sortedHead = head
        todoHead = head.next
        sortedHead.next = None

        while todoHead:
            todoNode = todoHead
            todoHead = todoHead.next
            todoNode.next = None
            self.insertPosition(todoNode, sortedHead)

        return sortedHead
