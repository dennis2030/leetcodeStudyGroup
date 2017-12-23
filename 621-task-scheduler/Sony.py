class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import defaultdict
        task_num = len(tasks)
        task_count = defaultdict(int)
        for task in tasks:
            task_count[task] += 1
        max_count = 0
        max_count_task_num = 0
        for task_count_item in task_count.items():
            if task_count_item[1] > max_count:
                max_count = task_count_item[1]
                max_count_task_num = 1
            elif task_count_item[1] == max_count:
                max_count_task_num += 1

        return max((n + 1) * (max_count - 1) + max_count_task_num, task_num)
