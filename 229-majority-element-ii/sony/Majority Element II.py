class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_filterd_diff_elem = 0
        group_num = 0
        element_num_map = dict()
        result_list = []
        target_num = int(len(nums) / 3) + 1

        for element in nums:
        	if element in element_num_map:
        		element_num_map[element] += 1
        	else:
        		if num_filterd_diff_elem >= 2:
        			group_num += 1
        			for key, value in element_num_map.items():
        				if value == 1:
        					del element_num_map[key]
        					num_filterd_diff_elem -= 1
        				else:
        					element_num_map[key] -= 1
        		else:
        			element_num_map[element] = 1


        # for element in nums:
        # 	if num_filterd_diff_elem >= 2:
        # 		if element in element_num_map:
        # 			element_num_map[element] += 1
        # 		else:
        # 			group_num += 1
        # 			for key, value in element_num_map.items():
        # 				if value == 1:
        # 					del element_num_map[key]
        # 					num_filterd_diff_elem -= 1
        # 				else:
        # 					element_num_map[key] -= 1
        # 	else:
        # 		if element in element_num_map:
        # 			element_num_map[element] += 1
        # 		else:
        # 			element_num_map[element] = 1
        # 			num_filterd_diff_elem += 1

        count_map = dict()
        for key, value in element_num_map.items():
        	if value >= target_num - group_num:
        		count_map[key] = 0
        for element in nums:
        	if element in count_map:
        		count_map[element] += 1

        for key, value in count_map.items():
        	if value >= target_num:
        		result_list.append(key)

        return result_list

if __name__ == '__main__':
	sol = Solution()
	nums = [1, 2, 3, 1, 1]
	print sol.majorityElement(nums)