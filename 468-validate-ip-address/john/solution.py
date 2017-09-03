class Solution(object):
    def isIPv4(self, IP):
        components = [r'(\d{1,3})'] * 4
        pattern = r'^{}$'.format(r'\.'.join(components))
        mo = re.match(pattern, IP)
        if mo is None:
            return False

        for group in mo.groups():
            if group == '0':
                continue
            if group.startswith('0'):
                return False
            number = int(group)
            if number >= 256:
                return False

        return True

    def isIPv6(self, IP):
        components = [r'([0-9a-fA-F]{1,4})'] * 8
        pattern = r'^{}$'.format(r':'.join(components))
        mo = re.match(pattern, IP)
        if mo is None:
            return False

        return True

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if self.isIPv4(IP):
            return 'IPv4'
        if self.isIPv6(IP):
            return 'IPv6'
        return 'Neither'
