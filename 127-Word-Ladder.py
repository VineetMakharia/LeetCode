from typing import List
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # First convert all of them to form h*t
        mappings = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                mappings[word[:i]+"*"+word[i+1:]].append(word)
        # print(mappings)
        seen = set()
        queue = collections.deque()
        queue.append((beginWord,1))
        while queue:
            # print(queue)
            word, k = queue.popleft()
            if word == endWord:
                return k
            if word not in seen:
                seen.add(word)
                for i in range(len(word)):
                    next_word = word[:i] + "*" + word[i+1:]
                    for nei in mappings[next_word]:
                        queue.append((nei,k+1))
        return 0

obj = Solution()
print(obj.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))
print(obj.ladderLength("hit","cog",["hot","dot","dog","lot","log"]))