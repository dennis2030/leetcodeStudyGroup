# Definition for singly-linked list.
class ListNode(object):
      def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node_num = 0
        cur_node = head
        while (cur_node != None):
            node_num += 1
            cur_node = cur_node.next

        target = node_num - n - 1
        if target < 0:
            head = head.next
        else:
            cur_node = head
            for i in xrange(target):
                cur_node = cur_node.next
            cur_node.next = cur_node.next.next
        return head





if __name__ == '__main__':
    sol = Solution()

    head = None
    cur_node = None
    m = 5
    for i in range(m):
        if i == 0:
            head = ListNode(i + 1)
            cur_node = head
        else:
            new_node = ListNode(i + 1)
            cur_node.next = new_node
            cur_node = new_node

#    cur_node = head
#    while cur_node != None:
#        print cur_node.val
#        cur_node = cur_node.next

    n = 2
    result = sol.removeNthFromEnd(head, n)
    cur_node = result
    while cur_node != None:
        print cur_node.val
        cur_node = cur_node.next