class Solution:
    
    @staticmethod
    def make_trie(words):
        root = dict()
        for idx, word in enumerate(words):
            current_dict = root
            for char in word:
                current_dict = current_dict.setdefault(char, {})
            current_dict['!'] = idx
        return root
    
    @staticmethod
    def check_concat(trie, word):
        cur = trie
        res = []
        prev = None
        
        for idx, char in enumerate(word):
            if char in cur:
                cur = cur[char]
                for next_char in cur:                
                    if next_char == '!':
                        if idx == len(word) - 1:
                            res.append(cur['!'])
                            return res
                        tmp = Solution.check_concat(trie, word[idx+1:])
                        
                        if tmp != []:
                            res.append(cur['!'])
                            res.extend(tmp)
                            return res
            else:
                return []
                    
                
        return res
    
    def findAllConcatenatedWordsInADict(self, words):
        l = len(words)
        words.sort(key = len, reverse = True)
        
        trie = Solution.make_trie(words)
        
        word_index_to_remove = []
        pos = 0
        res = []
        print(words)
        for word in words:
            tmp = Solution.check_concat(trie, word)
            print(word, tmp)
            if len(tmp) > 1: # the word is not concat
                res.append(word)

            pos += 1
        
        return res
        
            
        
if __name__ == '__main__':
    s = Solution()
    print(s.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
    print(s.findAllConcatenatedWordsInADict([""]))