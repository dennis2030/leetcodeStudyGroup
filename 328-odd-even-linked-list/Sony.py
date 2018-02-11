class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def convert(arr):
            list_head = ListNode(None)
            ptr = list_head
            for item in arr:
                ptr.next = ListNode(item)
                ptr = ptr.next
            return list_head, ptr
        odds = list()
        evens = list()
        node = head
        idx = 0
        while node is not None:
            if idx % 2 == 0:
                evens.append(node.val)
            else:
                odds.append(node.val)
            idx += 1
            node = node.next
        
        odds_head, odds_end = convert(odds)
        evens_head, evens_end = convert(evens)
        evens_end.next = odds_head.next
        
        return evens_head.next
