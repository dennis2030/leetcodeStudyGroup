# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        left_start = None
        left_end = None
        right_start = None
        right_end = None

        cur = head

        while cur != None:
            if cur.val < x:
                if left_start == None:
                    left_start = cur
                else:
                    left_end.next = cur

                left_end = cur
            else:
                if right_start == None:
                    right_start = cur
                else:
                    right_end.next = cur

                right_end = cur

            cur = cur.next

        if right_end != None:
            right_end.next = None

        if left_start != None:
            left_end.next = right_start

            return left_start

        return right_start
