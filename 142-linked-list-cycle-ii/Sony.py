#!/usr/bin/env python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            ptr1 = head.next
            ptr2= ptr1.next

            #find the first metting point
            while ptr1 != ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next.next

            #find perimeter
            ptr2 = ptr2.next
            perimeter = 1
            while ptr1 != ptr2:
                perimeter += 1
                ptr2 = ptr2.next

            #get to the point that is away from start with length equal to perimeter
            ptr2 = head
            for i in xrange(perimeter):
                ptr2 = ptr2.next

            #find first meeting point 
            ptr1 = head
            while ptr2 != ptr1:
                ptr1 = ptr1.next
                ptr2 = ptr2.next

            return ptr1

        except AttributeError:
            return None
