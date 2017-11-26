class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        result = {
            'best': -1
        }
        visited = [False] * len(bank)

        def diff1(gene1, gene2):
            return sum([char1 != char2 for char1, char2 in zip(gene1, gene2)]) == 1

        def recurse(curr, length):
            if curr == end:
                if result['best'] == -1 or length < result['best']:
                    result['best'] = length
                return

            for idx, gene in enumerate(bank):
                if visited[idx] or not diff1(curr, gene):
                    continue

                visited[idx] = True
                recurse(gene, length + 1)
                visited[idx] = False

        recurse(start, 0)

        return result['best']
