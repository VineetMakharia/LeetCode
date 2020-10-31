from typing import List
class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if px==py:
            return
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.rank[px]+=self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py]+=self.rank[px]
        
        
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        # Given that if the lengths are not equal then they are not similar
        if len(words1)!=len(words2):
            return False
        # Since they are words, we need to map them to a number
        hash_map = dict()
        idx = 0
        for word in (words1+words2):
            if word not in hash_map:
                hash_map[word] = idx
                idx+=1
        
        for x,y in pairs:
            if x not in hash_map:
                hash_map[x] = idx
                idx+=1
            if y not in hash_map:
                hash_map[y] = idx
                idx+=1
        # Build a disjoint set of the size of the hash map
        dsu = DSU(len(hash_map))
        
        # For every element in the pair, we need to connect them
        for x,y in pairs:
            dsu.union(hash_map[x],hash_map[y])
        
        # Iterate through the words, if any of the words don't share a similar parent, that means that the sentence is not similar
        for x,y in zip(words1,words2):
            if dsu.find(hash_map[x])!=dsu.find(hash_map[y]):
                return False
        return True

obj = Solution()
print(obj.areSentencesSimilarTwo(["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "good"], ["fine", "good"],\
     ["acting","drama"], ["skills","talent"]] ))