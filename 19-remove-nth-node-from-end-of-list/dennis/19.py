# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n <= 0:
            return head

        # Add a prev node of head to simplify the logic
        pPrevNodeOfHead = ListNode('prev node of head')
        pPrevNodeOfHead.next = head
        pPrevNodeOfDeletedNode = pPrevNodeOfHead

        pCurrentNode = head
        distanceOfTwoNode = 1
        while pCurrentNode.next != None:
            pCurrentNode = pCurrentNode.next
            distanceOfTwoNode += 1
            if distanceOfTwoNode > n:
                pPrevNodeOfDeletedNode = pPrevNodeOfDeletedNode.next

        pPrevNodeOfDeletedNode.next = pPrevNodeOfDeletedNode.next.next
        return pPrevNodeOfHead.next
