# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None

        odd_start = head
        odd_end = head
        even_start = head.next
        even_end = head.next

        head = head.next
        odd = True
        while head is not None:
            if odd:
                odd_end.next = head
                odd_end = head
            else:
                even_end.next = head
                even_end = head
            odd = not odd
            head = head.next

        odd_end.next = even_start
        if even_end is not None:
            even_end.next = None

        return odd_start
