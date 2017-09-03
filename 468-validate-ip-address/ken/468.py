class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        import re

        def isIPv4(IP):
            pattern = "^(\d+)\.(\d+)\.(\d+)\.(\d+)$"
            matches = re.findall(pattern, IP)

            if len(matches) == 0 or len(matches[0]) != 4:
                return False

            for match in matches[0]:
                if match.startswith('0') and len(match) > 1:
                    return False
                if int(match) > 255:
                    return False

            return True

        def isIPv6(IP):
            pattern = "^([\dabcdefABCDEF]+):([\dabcdefABCDEF]+):([\dabcdefABCDEF]+):([\dabcdefABCDEF]+):([\dabcdefABCDEF]+):([\dabcdefABCDEF]+):([\dabcdefABCDEF]+):([\dabcdefABCDEF]+)$"
            matches = re.findall(pattern, IP)

            if len(matches) == 0 or len(matches[0]) != 8:
                return False

            for match in matches[0]:
                if len(match) > 4:
                    return False

            return True

        if isIPv4(IP):
            return "IPv4"

        if isIPv6(IP):
            return "IPv6"

        return "Neither"
