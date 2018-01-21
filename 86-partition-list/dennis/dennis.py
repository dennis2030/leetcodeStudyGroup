# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):    
    def _print(self, head):
        ans = []
        node = head
        while node != None:
            ans.append(node.val)
            node = node.next
        return ans        
    
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        import sys
        fake_head = ListNode(-sys.maxint - 1)
        fake_head.next = head
        node = head
        prev = fake_head
        left_tail = None if head.val < x else head
        prev_left_tail = None if head.val < x else fake_head

        while node != None:
            if node.val >= x and left_tail == None:
                left_tail = node
                prev_left_tail = prev
            elif node.val < x and left_tail != None:                         
                # swap nodes                
                prev.next = node.next   
                prev_left_tail.next = node
                # handling boundary case
                if prev_left_tail == fake_head:
                    head = node
                prev_left_tail = node
                node.next = left_tail
                node = prev                
                                                                
            prev = node
            node = node.next
            
        return head
            
