class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        numExpect10 = 0
        for char in data:
            binary = format(char, '08b')
            if numExpect10 > 0:
                if binary.startswith('10'):
                    numExpect10 -= 1
                else:
                    return False
            else:
                if binary.startswith('0'):
                    numExpect10 = 0
                elif binary.startswith('110'):
                    numExpect10 = 1
                elif binary.startswith('1110'):
                    numExpect10 = 2
                elif binary.startswith('11110'):
                    numExpect10 = 3
                else:
                    return False
        return (numExpect10 == 0)
