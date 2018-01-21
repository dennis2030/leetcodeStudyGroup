class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        def assignNode(curr_node, next_val):
            if curr_node.val is None:
                curr_node.val = next_val
            else:
                curr_node.next = ListNode(next_val)
                curr_node = curr_node.next
            return curr_node
        curr_s = smaller_list = ListNode(None)
        curr_le = larger_equal_list = ListNode(None)
        curr = head
        while curr is not None:
            if curr.val >= x:
                curr_le = assignNode(curr_le, curr.val)
            else:
                curr_s = assignNode(curr_s, curr.val)
            curr = curr.next
        
        if larger_equal_list.val is None:
            larger_equal_list = None
        if curr_s.val is not None:
            curr_s.next = larger_equal_list
        else:
            smaller_list = larger_equal_list
        
        return smaller_list
