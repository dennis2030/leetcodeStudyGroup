class Solution(object):
    def replaceWords(self, _dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        from collections import defaultdict
        root_dict = defaultdict(list)
        for root in _dict:
            root_dict[root[0]].append(root)
                
        words = sentence.split()
        new_words = []
        matched_words = dict()
        for word in words:
            if word in matched_words:
                new_words.append(matched_words[word])
                continue

            new_word = word
            for root in root_dict[word[0]]:
                if new_word.startswith(root):
                    new_word = root
            matched_words[word] = new_word
            new_words.append(new_word)
        
        return ' '.join(new_words)
