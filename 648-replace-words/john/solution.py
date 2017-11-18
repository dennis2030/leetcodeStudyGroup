class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        realDict = set()

        def findRoot(word):
            for root in realDict:
                if word.startswith(root):
                    return root
            return None

        for root in sorted(dict, key=len):
            if findRoot(root) is None:
                realDict.add(root)

        result = []
        for word in sentence.split():
            root = findRoot(word)
            if root is None:
                result.append(word)
            else:
                result.append(root)

        return ' '.join(result)
