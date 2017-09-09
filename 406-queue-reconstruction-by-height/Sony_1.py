class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        tall_list =[]
        tall_map = dict()
        for person in people:
            tall = person[0]
            if tall not in tall_map:
                tall_map[tall] = list()
                tall_list.append(tall)
            tall_map[tall].append(person[1])
        tall_list.sort(key=lambda x: -x)

        for tall in tall_list:
            tall_map[tall].sort()
            for idx in tall_map[tall]:
                result.insert(idx, [tall, idx])

        return result

if __name__ == '__main__':

    sol = Solution()

    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    print sol.reconstructQueue(people)