# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        oddHead = oddTail = head
        evenHead = evenTail = head.next

        curr = head.next.next
        isOdd = True
        while curr is not None:
            if isOdd:
                oddTail.next = curr
                oddTail = oddTail.next
            else:
                evenTail.next = curr
                evenTail = evenTail.next

            curr = curr.next
            isOdd = not isOdd

        oddTail.next = evenHead
        evenTail.next = None

        return oddHead
