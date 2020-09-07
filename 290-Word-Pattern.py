class Solution:
    def wordPattern(self, pattern, str):
        words = str.split()
        if len(words)!=len(pattern):
            return False
        
        hash_map = dict()
        for i in range(len(pattern)):
            if pattern[i] not in hash_map:
                if words[i] in hash_map.values():
                    return False
                else:
                    hash_map[pattern[i]] = words[i]
            else:
                if hash_map[pattern[i]]!=words[i]:
                    return False
        return True

obj = Solution()
print(obj.wordPattern("abba","dog cat cat dog"))
print(obj.wordPattern("abba","dog cat cat fish"))