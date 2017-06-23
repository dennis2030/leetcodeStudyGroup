class Solution(object):
	def isValidSerialization(self, preorder):
		"""
		:type preorder: str
		:rtype: bool
		"""

		def checkByRecursive(tokens):
			def Recursive(tokens):
				if len(tokens) == 0:
					return False

				if tokens.pop(0) == '#':
					return True

				if len(tokens) < 2 or \
				   Recursive(tokens) == False or \
				   Recursive(tokens) == False:
					return False

				return True

			if Recursive(tokens) == False or len(tokens) > 0:
				return False
			return True

		def checkByCnt(tokens):
			if tokens.pop(0) == '#':
				return len(tokens) == 0

			cnt = 2
			for token in tokens:
				if cnt == 0:
					return False
				if token == '#':
					cnt -= 1
				else:
					cnt += 1

			return cnt == 0


		tokens = preorder.split(",")
		# ret = checkByRecursive(tokens)
		ret = checkByCnt(tokens)

		return ret
