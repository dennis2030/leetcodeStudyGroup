# Definition for singly-linked list.
# class ListNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.next = None

class Solution(object):
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""

		target = head
		p = head

		for i in xrange(n + 1):
			if not p:
				head = head.next
				return head
			p = p.next

		while p:
			p = p.next
			target = target.next

		target.next = target.next.next


		return head
