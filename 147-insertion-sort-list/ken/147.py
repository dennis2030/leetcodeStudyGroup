# Definition for singly-linked list.
# class ListNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.next = None

class Solution(object):
	def insertionSortList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""

		if head is None:
			return None

		new_head = head
		cur = head.next
		new_head.next = None

		while cur:
			next = cur.next

			if cur.val <= new_head.val:
				cur.next = new_head
				new_head = cur
			else:
				i = new_head
				while i:
					if i.next is None or cur.val <= i.next.val:
						cur.next = i.next
						i.next = cur
						break
					i = i.next

			cur = next

		return new_head