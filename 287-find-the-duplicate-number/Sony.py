class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math

        min_num = 1
        max_num = len(nums) - 1
        while min_num != max_num:
            middle = (min_num + max_num) / 2
            smaller_cnt = 0
            for num in nums:
                if num <= middle:
                    smaller_cnt += 1

            if smaller_cnt > middle:
                max_num = middle
            else:
                min_num = middle + 1
        return min_num


if __name__ == '__main__':

    sol = Solution()

    nums = [1,2,4,3,5,9,6,7,8,2]
    print sol.findDuplicate(nums)