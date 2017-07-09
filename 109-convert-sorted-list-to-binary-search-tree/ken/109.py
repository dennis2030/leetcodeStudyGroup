# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def sortedListToBST(self, head):
		"""
		:type head: ListNode
		:rtype: TreeNode
		"""

		def getNodeNum(head):
			NodeNum = 0

			while head != None:
				head = head.next
				NodeNum += 1

			return NodeNum

		def getNodeBeforeMedium(head):
			NodeNum = getNodeNum(head)
			midPrevNode = head

			for i in xrange(NodeNum / 2 - 1):
				midPrevNode = midPrevNode.next

			return midPrevNode

		if head is None:
			return None

		if head.next is None:
			return TreeNode(head.val)

		midPrevNode = getNodeBeforeMedium(head)
		root = TreeNode(midPrevNode.next.val)
		root.right = self.sortedListToBST(midPrevNode.next.next)
		midPrevNode.next = None
		root.left = self.sortedListToBST(head)

		return root
