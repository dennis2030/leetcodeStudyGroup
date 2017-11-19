class Solution(object):
    
    def constructTrie(self, d):        
        root_trie = {}
        for s in d:
            current_trie = root_trie
            for c in s:
                current_trie = current_trie.setdefault(c, {})
            current_trie['has_word'] = True
            
        return root_trie
                
                
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        result = []
        root_trie = self.constructTrie(dict)        
        for word in sentence.split(' '):
            current_trie = root_trie
            tmp_prefix = []
            for c in word:                                
                if 'has_word' in current_trie:
                    word = ''.join(tmp_prefix)
                    break
                if c not in current_trie:                    
                    break                                
                    
                current_trie = current_trie[c]
                tmp_prefix.append(c)
            result.append(word)
        return ' '.join(result).strip()
