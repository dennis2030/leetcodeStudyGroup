class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        return self.leastInterval_2(self, tasks, n)

    def leastInterval_1(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import defaultdict

        taskNum = defaultdict(int)
        intervals = dict()
        ans = 0
        total = len(tasks)

        for task in tasks:
            taskNum[task] += 1
            intervals[task] = -1

        while True:
            maxNum = 0
            maxCh = None
            for ch in taskNum:
                num = taskNum[ch]
                if (intervals[ch] == -1 or ans - intervals[ch] > n) and num > maxNum:
                    maxNum = num
                    maxCh = ch

            if total == 0:
                break

            if maxCh is not None:
                intervals[maxCh] = ans
                taskNum[maxCh] -= 1
                total -= 1

            ans += 1

        return ans

    def leastInterval_2(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        taskNum = dict.fromkeys('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 0)
        for task in tasks:
            taskNum[task] += 1

        v = taskNum.values()
        v.sort(reverse=True)
        numOfMostFreqTask = v[0]
        numOfMaxTask = v.count(numOfMostFreqTask)
        totalMaxTask = numOfMostFreqTask * numOfMaxTask
        remainTasks = len(tasks) - totalMaxTask

        segWidth = (n + 1)
        numOfSeg = (numOfMostFreqTask - 1)

        spaceInSeg = segWidth - numOfMaxTask
        totalSpaces = spaceInSeg * numOfSeg
        extraSpace = 0
        if remainTasks > totalSpaces:
            extraSpace = remainTasks - totalSpaces

        return segWidth * numOfSeg + numOfMaxTask + extraSpace
