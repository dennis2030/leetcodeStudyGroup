class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = []

        heights = sorted(list(set([person[0] for person in people])), reverse=True)

        for height in heights:
            group = []
            for person in people:
                if person[0] == height:
                    group.append(person)

            group = sorted(group, key=lambda person: person[1])
            for person in group:
                queue.insert(person[1], person)

        return queue
