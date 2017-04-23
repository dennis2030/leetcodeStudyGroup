class Solution(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""

		if len(digits) == 0:
			return []

		m = {}
		m['0'] = [' ']
		m['1'] = ['*']
		m['2'] = ['a', 'b', 'c']
		m['3'] = ['d', 'e', 'f']
		m['4'] = ['g', 'h', 'i']
		m['5'] = ['j', 'k', 'l']
		m['6'] = ['m', 'n', 'o']
		m['7'] = ['p', 'q', 'r', 's']
		m['8'] = ['t', 'u', 'v']
		m['9'] = ['w', 'x', 'y', 'z']

		res = ['']
		for digit in digits:
			new_res = []
			for r in res:
				for c in m[digit]:
					new_res.append(r+c)
			res = new_res

		return res
