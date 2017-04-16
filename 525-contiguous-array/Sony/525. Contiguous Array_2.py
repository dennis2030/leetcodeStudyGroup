class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        sum_idx_map = {0:-1}
        now_sum = 0
        max_value = 0

        for i in xrange(nums_len):
            if nums[i] == 0:
                nums[i] = -1

        for idx, num in enumerate(nums):
            now_sum += num
            if now_sum in sum_idx_map:
                max_value = max(max_value, idx - sum_idx_map[now_sum])
            else:
                sum_idx_map[now_sum] = idx

        return max_value



if __name__ == '__main__':
    sol = Solution()


    nums = [0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]

    print sol.findMaxLength(nums)