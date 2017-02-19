class Solution(object):
    def append_zeros(self, input_list, expect_len):
        for i in xrange(expect_len - len(input_list)):
            input_list.append(0)

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_list = version1.split('.')
        v2_list = version2.split('.')
        max_len = max(len(v1_list), len(v2_list))
        self.append_zeros(v1_list, max_len)
        self.append_zeros(v2_list, max_len)

        for i in xrange(max_len):
            if int(v1_list[i]) > int(v2_list[i]):
                return 1
            elif int(v1_list[i]) < int(v2_list[i]):
                return -1

        return 0
