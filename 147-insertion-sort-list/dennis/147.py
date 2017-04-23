# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def printList(self, head):
        current = head
        tmp_str = ''
        while current != None:
            tmp_str += str(current.val)
            current = current.next
        print tmp_str
        
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return head
        
        preHead = ListNode(-1)
        preHead.next = head
        sorted_tail = head
        to_be_inserted = head.next
        
        while to_be_inserted != None:
            current = head
            previous = preHead
            
            needToChange = False
            while current != sorted_tail.next:
                if current.val > to_be_inserted.val:
                    needToChange = True
                    break
                previous = current
                current = current.next
            
            if needToChange:
                # change pos in-place
                sorted_tail.next = to_be_inserted.next
                previous.next = to_be_inserted
                to_be_inserted.next = current
                if current == head:
                    head = to_be_inserted
                    preHead.next = head
            # go to next round
            else:
                sorted_tail = to_be_inserted
            
            to_be_inserted = sorted_tail.next
            
        return head
            
