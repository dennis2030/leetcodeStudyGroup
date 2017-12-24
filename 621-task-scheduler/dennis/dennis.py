from collections import defaultdict
class Solution(object):
    def constructTaskDict(self, tasks):
        task_dict = {}
        for t in tasks:
            # initialization
            if t not in task_dict:
                task_dict[t] = {}
                task_dict[t]['count'] = 0
                task_dict[t]['last_index'] = -101
            task_dict[t]['count'] += 1
        return task_dict        
    
    def findMaxCount(self, task_dict, idx, n):
        champion = 0
        championKey = ''
        for key in task_dict:
            # skip this key since it's cooling down
            if task_dict[key]['last_index'] + n >= idx:
                continue
            if task_dict[key]['count'] > champion:
                champion = task_dict[key]['count']
                championKey = key        
        return championKey
    
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_dict = self.constructTaskDict(tasks)        
        remain = len(tasks)
        idx = 0
        while remain > 0:
            maxKey = self.findMaxCount(task_dict, idx, n)                 
            if maxKey != '':
                task_dict[maxKey]['count'] -= 1
                task_dict[maxKey]['last_index'] = idx
                remain -= 1
                        
            idx += 1
        return idx
        
