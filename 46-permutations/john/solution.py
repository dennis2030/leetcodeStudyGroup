class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def generator(used):
            if len(used) == len(nums):
                yield []
                return

            for num in nums:
                if num in used:
                    continue
                used.add(num)
                for perm in generator(used):
                    yield [num] + perm
                used.remove(num)

        return list(generator(set()))
