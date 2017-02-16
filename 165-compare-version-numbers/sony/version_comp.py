#!/usr/bin/python
#https://leetcode.com/problems/compare-version-numbers/

class Version(object):
    def __init__(self, ver):
        version_token = ver.split('.')
        self.version_map = [int(x) for x in version_token]
        self.version_map_len = len(self.version_map)

    def expanded_version_map(self, length):
        new_map = [0] * length
        for i in range(self.version_map_len):
            new_map[i] = self.version_map[i]
        return new_map

    def gen_comparing_arg(self, other):
        self_new_map = self.version_map
        other_new_map = other.version_map
        compared_len = self.version_map_len
        if (self.version_map_len < other.version_map_len):
            self_new_map = self.expanded_version_map(other.version_map_len)
            compared_len = other.version_map_len
        elif (self.version_map_len > other.version_map_len):
            other_new_map = other.expanded_version_map(self.version_map_len)
        return compared_len, self_new_map, other_new_map

    def __lt__(self, other):
        less_than = True
        compared_len, self_new_map, other_new_map = self.gen_comparing_arg(other)
        for i in range(compared_len):
            if self_new_map[i] > other_new_map[i]:
                less_than = False
                break
            elif self_new_map[i] < other_new_map[i]:
                break
            if i + 1 == compared_len:
                less_than = self_new_map[i] != other_new_map[i]

        return less_than

    def __le__(self, other):
        less_equal = True
        compared_len, self_new_map, other_new_map = self.gen_comparing_arg(other)
        for i in range(compared_len):
            if self_new_map[i] > other_new_map[i]:
                less_equal = False
                break
            elif self_new_map[i] < other_new_map[i]:
                break

        return less_equal

    def __eq__(self, other):
        the_same = True
        compared_len, self_new_map, other_new_map = self.gen_comparing_arg(other)
        for i in range(compared_len):
            if self_new_map[i] != other_new_map[i]:
                the_same = False
                break
        return the_same

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other


class Solution(object):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    def compareVersion(self, version1, version2):
        v1 = Version(version1)
        v2 = Version(version2)
        if (v1 > v2):
            print 1
        elif (v1 < v2):
            print -1
        else:
            print 0


if __name__ == '__main__':
    sol = Solution()
    v1 = raw_input('v1:')
    v2 = raw_input('v2:')
    sol.compareVersion(v1, v2)
