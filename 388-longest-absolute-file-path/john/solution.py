class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        def parseLine(line):
            match = re.match(r'^(\t*)(.+)$', line)
            tabs = match.group(1)
            name = match.group(2)
            depth = len(tabs) + 1
            isLeaf = ('.' in name)
            return name, depth, isLeaf

        lines = input.split('\n')
        maxLength = 0
        stack = []
        for line in lines:
            name, depth, isLeaf = parseLine(line)
            while len(stack) >= depth:
                stack.pop()
            stack.append(name)
            if isLeaf:
                maxLength = max(maxLength, len('/'.join(stack)))

        return maxLength
