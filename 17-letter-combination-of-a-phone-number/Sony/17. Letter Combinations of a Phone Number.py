class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_alpha = {
            '0': [' '],
            '1': ['*'],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if len(digits) == 0:
            return []

        cur_result = set([''])
        for idx, char in enumerate(digits):
            variables = digit_alpha[char]
            combination = set()
            for item in cur_result:
                for variable in variables:
                    combination.add(item + variable)

            cur_result = combination

        return list(cur_result)


if __name__ == '__main__':

    sol = Solution()


    digits = '22'
    print sol.letterCombinations(digits)