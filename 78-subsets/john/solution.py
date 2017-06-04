class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        def recurse(curr, idx):
            if idx == len(nums):
                result.append(list(curr))
                return

            recurse(curr, idx + 1)

            curr.append(nums[idx])
            recurse(curr, idx + 1)
            curr.pop()


        recurse([], 0)

        return result
