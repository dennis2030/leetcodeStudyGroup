import Queue
class Solution(object):
    def canMutate(self, str_1, str_2):
        distance = 0
        for i in xrange(len(str_1)):
            if str_1[i] != str_2[i]:
                distance += 1
        return (distance <= 1)
            
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        # run BFS to traverse through the bank
        
        num_mutation = 0
        
        q = Queue.Queue()
        q.put(start)
        
        while q.qsize() != 0 and num_mutation <= len(bank):            
            for i in xrange(q.qsize()):
                tmp_mutation = q.get()
                if tmp_mutation == end:
                    return num_mutation
                for b in bank:
                    if self.canMutate(tmp_mutation, b):
                        q.put(b)            

            num_mutation += 1
        return -1 # not found
