class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import defaultdict
        task_num = len(tasks)
        if task_num == 0:
            return 0
        task_count = defaultdict(int)
        for task in tasks:
            task_count[task] += 1
        task_count = task_count.items()
        task_type_num = len(task_count)
        task_count.sort(key=lambda x: -x[1])
        
        interval = 0
        max_count = task_count[0][1]
        max_count_task_num = 0
        for task_count_item in task_count:
            if task_count_item[1] < max_count:
                break
            max_count_task_num += 1
        return max((n + 1) * (max_count - 1) + max_count_task_num, task_num)
