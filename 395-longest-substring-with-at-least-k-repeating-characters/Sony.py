class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        char_loc_map = {}
        for idx, _char in enumerate(s):
            if _char not in char_loc_map:
                char_loc_map[_char] = list()
            char_loc_map[_char].append(idx)
        deli_list = [len(s)]
        for _char in char_loc_map:
            if len(char_loc_map[_char]) < k:
                deli_list += char_loc_map[_char]
        if len(deli_list) == 1:
            return len(s)
        deli_list.sort()
        max_length = 0
        start_idx = -1
        for end_idx in deli_list:
            if end_idx - start_idx - 1 > max_length:
                length = self.longestSubstring(s[start_idx + 1: end_idx], k)
                if length > max_length:
                    max_length = length
            start_idx = end_idx
        return max_length


if __name__ == '__main__':

    sol = Solution()

    s = "ababbc"
    k = 2
    print sol.longestSubstring()