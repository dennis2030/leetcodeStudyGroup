class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """

        ans = []
        dict.sort()

        tokens = sentence.split()
        for token in tokens:
            for root in dict:
                if token.startswith(root):
                    token = root
                    break
            ans.append(token)

        return ' '.join(ans)
