class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        def validate_word(data, data_len, start_idx):
            cur_idx = start_idx
            left_byte = 0
            if data[cur_idx] < 128:
                return True, cur_idx + 1
            elif data[cur_idx] < 192:
                return False, 0
            elif data[cur_idx] < 224:
                left_byte = 1
            elif data[cur_idx] < 240:
                left_byte = 2
            elif data[cur_idx] < 248:
                left_byte = 3
            else:
                return False, 0
            cur_idx += 1
            while left_byte > 0:
                if cur_idx >= data_len or data[cur_idx] < 128 or data[cur_idx] >= 192:
                    return False, 0
                cur_idx += 1
                left_byte -= 1
            return True, cur_idx
        data_len = len(data)
        idx = 0

        while idx < data_len:
            valid, idx = validate_word(data, data_len, idx)
            if not valid:
                return False

        return True




if __name__ == '__main__':

    sol = Solution()
    data = [197, 130, 1]
    #data = [235, 140, 4]
    print sol.validUtf8(data)