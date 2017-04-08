class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def parseInt(string):
            int_val = int(string)

            if len(str(int_val)) != len(string):
                return 555 #a invalid value
            else:
                return int_val

        def genSegment(seg_left, in_str):
            result = list()
            if seg_left * 3 < len(in_str) or len(in_str) == 0:
                return []

            if seg_left > 1:
                for i in xrange(1, 4):
                    prefix = in_str[0:i]
                    suffix = in_str[i:]
                    int_val = parseInt(prefix)
                    if int_val > 255:
                        continue

                    ret = genSegment(seg_left - 1, suffix)
                    for sub_str in ret:
                        result.append(prefix + '.' + sub_str)
            elif parseInt(in_str) <= 255:
                result.append(in_str)

            return result

        return genSegment(4, s)

if __name__ == '__main__':
    sol = Solution()

    ip = "0000"

    print sol.restoreIpAddresses(ip)