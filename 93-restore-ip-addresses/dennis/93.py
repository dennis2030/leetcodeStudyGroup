#!/usr/bin/env python2.7
class Solution(object):
    def isValidIP(self, s):
        if not s or str(int(s)) != s or int(s) > 255 or int(s) < 0:
            return False
        return True

    def recursiveFindValidIP(self, s, level):
        if level == 4:
            if self.isValidIP(s):
                return [[s]]
            else:
                return [[]]

        valid_ips = []
        for i in xrange(1, min(len(s), 3) + 1):
            tmp_ip = s[:i]
            if not self.isValidIP(tmp_ip):
                continue
            tmp_list = []
            combinations = self.recursiveFindValidIP(s[i:], level + 1)
            for comb in combinations:
                tmp_list.append([tmp_ip] + comb)
            valid_ips += tmp_list
        return valid_ips

    def restoreIpAddresses(self, s):
        return [str('.').join(x) for x in self.recursiveFindValidIP(s, 1) if len(x) == 4]

sol = Solution()
print sol.restoreIpAddresses('2552552555')
