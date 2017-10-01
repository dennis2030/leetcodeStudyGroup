class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        prefix = []
        inputs = input.split("\n")
        longest = 0

        for i in inputs:
            tokens = i.split("\t")

            while len(prefix) >= len(tokens):
                prefix.pop()
            prefix.append(tokens[-1])

            if "." in tokens[-1]:
                path = "/".join(prefix)
                longest = max(longest, len(path))

        return longest


a = Solution()
a.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
