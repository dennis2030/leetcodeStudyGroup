class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        def canTransform(ori, new):
            diff = 0
            for i in xrange(8):
                if ori[i] != new[i]:
                    diff += 1
            return diff == 1

        new_bank = list()
        bfs_list = [(start, 1)]
        for gene in bank:
            new_bank.append((gene, gene == end))
            
        while len(bfs_list) > 0:
            cur_gene, step = bfs_list.pop(0)
            another_bank = list()
            for test_gene, is_end in new_bank:
                if canTransform(cur_gene, test_gene):
                    if is_end:
                        return step
                    else:
                        bfs_list.append((test_gene, step + 1))
                else:
                    another_bank.append((test_gene, is_end))
            new_bank = another_bank
        return -1
