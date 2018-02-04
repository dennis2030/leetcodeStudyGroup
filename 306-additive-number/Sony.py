class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def validAdditive(num, num_len, next_start, num1, num2):
            next_num = "{0}".format(num1 + num2)
            next_num_len = len(next_num)
            if next_start + next_num_len > num_len:
                return -1
            for idx, digit in enumerate(next_num):
                if digit != num[next_start + idx]:
                    return -1
            return next_start + next_num_len

        num_len = len(num)
        if num_len < 3:
            return False
        
        for i in xrange(1, num_len - 1):
            for j in xrange(i + 1, num_len):
                num1 = int(num[:i])
                num2 = int(num[i:j])
                if (i > 1  and num[0] == "0") or ((j - i > 1) and num[i] == "0"):
                    continue
                next_start = j
                while True:
                    next_start = validAdditive(num, num_len, next_start, num1, num2)
                    if next_start == -1:
                        break
                    elif next_start == num_len:
                        return True
                    else:
                        tmp_num = num1
                        num1 = num2
                        num2 = tmp_num + num2
        return False
