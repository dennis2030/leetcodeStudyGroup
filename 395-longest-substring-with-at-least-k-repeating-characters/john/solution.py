class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result = {'answer': ''}

        def findMinors(string):
            counts = {}
            for char in string:
                if char not in counts:
                    counts[char] = 1
                else:
                    counts[char] += 1

            minors = set()
            for char in counts:
                if counts[char] < k:
                    minors.add(char)

            return minors

        def cut(string, minors):
            substring = ''
            for char in string:
                if char not in minors:
                    substring += char
                elif len(substring) > 0:
                    yield substring
                    substring = ''
            if len(substring) > 0:
                yield substring

        def recurse(string):
            if len(result['answer']) > len(string):
                return

            minors = findMinors(string)
            if not minors:
                result['answer'] = string
                return

            for substring in cut(string, minors):
                recurse(substring)

        recurse(s)

        return len(result['answer'])
