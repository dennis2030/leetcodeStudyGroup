class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        valid = True
        i = 0

        while i < len(data) and valid:
            binText = format(data[i], 'b').zfill(8)
            i += 1
            num = 0

            if binText.startswith("0"):
                continue
            elif binText.startswith("110"):
                num = 1
            elif binText.startswith("1110"):
                num = 2
            elif binText.startswith("11110"):
                num = 3
            else:
                valid = False
                break

            if len(data) - i < num:
                valid = False
                break

            for j in xrange(num):
                binText = format(data[i], 'b').zfill(8)
                i += 1

                if not binText.startswith("10"):
                    valid = False
                    break

        return valid
