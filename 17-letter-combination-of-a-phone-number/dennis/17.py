import Queue
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) <= 0:
            return []
            
        mapping_dict = {
            '0': [' '],
            '1': ['*'],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        q = Queue.Queue()
        for c in mapping_dict[digits[0]]:
            q.put(c)
            
        for c in digits[1:]:
            options = mapping_dict[c]
            size_of_this_round = q.qsize()
            for i in xrange(size_of_this_round):
                candidate = q.get()
                for option in options:
                    q.put(candidate + option)

        result_list = []
        while not q.empty():
            result_list.append(q.get())
            
        return result_list
