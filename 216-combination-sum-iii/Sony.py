# vary slow, should refine it
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def goDeeper(nums_left, sum_left, start, stop, cand_list, result_list):
            for i in xrange(start, stop + 1):
                if i > sum_left:
                    break
                cand_list.append(i)
                curr_sum_left = sum_left - i
                if nums_left == 1 and curr_sum_left == 0:
                    result_list.append(list(cand_list))
                elif nums_left > 1:
                    goDeeper(nums_left - 1, curr_sum_left, i + 1, stop, cand_list, result_list)
                cand_list.pop()
        result_list = list()
        goDeeper(k, n, 1, 9, [], result_list)
        return result_list
