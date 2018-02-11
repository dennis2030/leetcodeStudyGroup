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
        
        if not head or not head.next:
            return head
        
        even_head = head.next
        
        odd_tail = head
        even_tail = head.next
        node = head.next.next
        # start from the third node
        idx = 3
        while node != None:
            # case odd number
            if idx % 2 == 1:
                odd_tail.next = node
                odd_tail = node
            # case even number
            elif idx % 2 == 0:
                even_tail.next = node
                even_tail = node
                            
            node = node.next
            idx += 1
        odd_tail.next = even_head
        even_tail.next = None
        return head
