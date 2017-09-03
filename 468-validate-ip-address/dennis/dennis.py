import re
class Solution(object):
    def isIPV4(self, IP):
        pattern = '^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$'        
        if not re.search(pattern, IP):
            return False
        parts = IP.split('.')
        for part in parts:
            int_rep = int(part)
            if (len(part) > 1 and part[0] == '0') or (int_rep > 255):
                return False
            
        return True
            
    def isIPV6(self, IP):
        pattern = '^[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}$'
        if not re.search(pattern, IP):
            return False
        return True
    
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
                
        result = 'Neither'
        if self.isIPV4(IP):
            result = 'IPv4'
        if self.isIPV6(IP):
            result = 'IPv6'
        return result
