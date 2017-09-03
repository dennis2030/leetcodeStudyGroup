class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        import re
        str_len = len(IP)
        if str_len < 7 or str_len > 39:
            return "Neither"

        v4_pattern = '^' + '.'.join(['([1-9][0-9]*|0)' for i in xrange(4)]) + '$'
        v4_match = re.match(v4_pattern, IP)
        if v4_match:
            return 'IPv4' if all(map(lambda x: int(x) < 256, v4_match.groups())) else "Neither"

        v6_pattern = '^' + ':'.join(["([0-9A-Fa-f][0-9A-Fa-f]{0,3})" for i in xrange(8)]) + '$'
        v6_match = re.match(v6_pattern, IP)
        return "IPv6" if v6_match else "Neither"


if __name__ == '__main__':

    sol = Solution()

    IP = '192.168.0.1'
    print sol.validIPAddress(IP)