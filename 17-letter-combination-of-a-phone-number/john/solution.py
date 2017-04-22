class Solution(object):
    def recurse(self, digits, results, curr):
        if len(curr) == len(digits):
            results.append(curr)
            return

        choices = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        idx = len(curr)
        for key in choices[digits[idx]]:
            self.recurse(digits, results, curr + key)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        results = []
        if len(digits) == 0:
            return results
        self.recurse(digits, results, '')
        return results
