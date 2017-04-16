# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        cur_node = head.next
        head.next = None

        while cur_node is not None:
            print 'cur_node is', cur_node.val
            next_node = cur_node.next
            cur_node.next = None
            pre_compare_node = None
            compare_node = head
            while compare_node != cur_node and compare_node is not None:
                if compare_node.val >= cur_node.val:
                    if pre_compare_node is not None:
                        pre_compare_node.next = cur_node
                        cur_node.next = compare_node
                    else:
                        cur_node.next = head
                        head = cur_node
                    break
                pre_compare_node = compare_node
                compare_node = compare_node.next
            if compare_node is None:
                pre_compare_node.next = cur_node
            cur_node = next_node
        the_node = head
        while the_node is not None:
            print the_node.val,
            the_node = the_node.next


        return head


if __name__ == '__main__':
    nums = [3,2,4]

    head = ListNode(nums[0])
    cur_node = head
    for i in range(1, len(nums)):
        cur_node.next = ListNode(nums[i])
        cur_node = cur_node.next
    sol = Solution()
    sol.insertionSortList(head)