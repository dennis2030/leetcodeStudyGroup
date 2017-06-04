class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import Queue
        results = []
        q = Queue.Queue()
        q.put([])
        for num in nums:
            size_this_round = q.qsize()
            for i in xrange(size_this_round):
                tmp_list = q.get()
                list_no_num = list(tmp_list)
                q.put(list_no_num)
                list_has_num = list(tmp_list)
                list_has_num.append(num)
                q.put(list_has_num)
        while not q.empty():
            results.append(q.get())
        return results
