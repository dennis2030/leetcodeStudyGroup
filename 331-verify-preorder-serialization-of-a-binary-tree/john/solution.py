class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        elems = preorder.split(',')

        stack = []
        while elems:
            stack.append(elems.pop(0))

            while len(stack) >= 3 and stack[-2:] == ['#', '#'] and stack[-3] != '#':
                stack[-3] = '#'
                stack.pop()
                stack.pop()

        return len(stack) == 1 and stack[0] == '#'
