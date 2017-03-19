class Solution(object):
    def get_nth_element(self, nums, n):
    	from heapq import nlargest
    	return nlargest(n, nums)[-1]

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        list_len = len(nums)
        nth_element = self.get_nth_element(nums, list_len / 2 + list_len % 2)

        smaller_list = list()
       	larger_list = list()
        for num in nums:
        	if num > nth_element:
        		larger_list.append(num)
        	elif num < nth_element:
        		smaller_list.append(num)

        smaller_len = len(smaller_list)
        larger_len = len(larger_list)
        append_len = list_len / 2 - smaller_len + list_len % 2
        smaller_list = [nth_element] * append_len + smaller_list
        larger_list = larger_list + [nth_element] * (list_len / 2 - larger_len)

        get_from_larger = False
        for i in xrange(list_len):
        	if get_from_larger:
        		nums[i] = larger_list[i / 2]
        		get_from_larger = False
        	else:
        		nums[i] = smaller_list[i / 2]
        		get_from_larger = True
        print nums



if __name__ == '__main__':
    sol = Solution()
    nums = [1,1,2,1,2,2,1]
    sol.wiggleSort(nums)