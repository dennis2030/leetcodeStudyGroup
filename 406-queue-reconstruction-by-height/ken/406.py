class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        queue = []
        people.sort(key = lambda x : (-x[0], x[1]))

        for i in xrange(len(people)):
            height = people[i][0]
            cnt = people[i][1]
            idx = 0

            for j in xrange(len(queue)):
                if cnt == 0:
                    break
                cnt -= 1
                idx += 1

            queue.insert(idx, people[i])

        return queue
