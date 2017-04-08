class Solution(object):
	def restoreIpAddresses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""

		def validSection(sectionStr):
			if sectionStr == '':
				return False
			if sectionStr[0] == '0' and len(sectionStr) != 1:
				return False

			if int(sectionStr) > 255:
				return False

			return True

		def Recursive(s, sectionNum):
			if sectionNum == 4:
				if validSection(s):
					return [s]
				return []

			Res = []
			for i in xrange(1, 4):
				sectionStr = s[:i]
				RemainStr = s[i:]

				if validSection(sectionStr):
					subIPs = Recursive(RemainStr, sectionNum + 1)
					for subIP in subIPs:
						Res.append(sectionStr + '.' + subIP)

			return Res

		return Recursive(s, 1)
