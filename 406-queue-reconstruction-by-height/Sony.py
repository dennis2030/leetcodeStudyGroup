class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        num_people = len(people)
        people.sort(key=lambda person: [person[0], -person[1]])
        print people
        new_people = []
        result = []

        for person in people:
            new_people.append([person[1], person])

        for idx in xrange(num_people + 1):
            for new_idx, new_person in enumerate(new_people):
                if new_person[0] == 0:
                    result.append(new_person[1])
                    new_people.pop(new_idx)
                    break
                else:
                    new_person[0] -= 1

        return result


if __name__ == '__main__':

    sol = Solution()

    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    print sol.reconstructQueue(people)