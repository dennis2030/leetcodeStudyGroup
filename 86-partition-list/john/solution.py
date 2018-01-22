i# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def convert(self, vals):
        dummy = ListNode(5566)
        curr = dummy
        for val in vals:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smalls = []
        bigs = []
        curr = head
        while curr is not None:
            if curr.val < x:
                smalls.append(curr.val)
            else:
                bigs.append(curr.val)
            curr = curr.next

        return self.convert(smalls + bigs)
