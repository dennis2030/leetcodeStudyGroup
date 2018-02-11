class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly_list = [1]
        idx_2 = 0
        idx_3 = 0
        idx_5 = 0
        i = 1
        num_2 = 2 * ugly_list[idx_2]
        num_3 = 3 * ugly_list[idx_3]
        num_5 = 5 * ugly_list[idx_5]
        while i < n:
            min_num = min([num_2, num_3, num_5])
            ugly_list.append(min_num)
            if min_num == num_2:
                idx_2 += 1
                num_2 = 2 * ugly_list[idx_2]
            if min_num == num_3:
                idx_3 += 1
                num_3 = 3 * ugly_list[idx_3]
            if min_num == num_5:
                idx_5 += 1
                num_5 = 5 * ugly_list[idx_5]
            i += 1
            
        return ugly_list[n - 1]
