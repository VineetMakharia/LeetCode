class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        rx = self.rank[x]
        ry = self.rank[y]
        if px!=py:
            if rx>ry:
                self.parent[py]=px
                self.rank[px]+=self.rank[py]
            else:
                self.parent[px]=py
                self.rank[py]+=self.rank[px]
    
class Solution:
    def longestConsecutive(self, nums):
        if len(nums)==0:
            return 0
        nums = set(nums)
        hash_map = dict()
        dsu = DSU(len(nums))
        for idx,num in enumerate(nums):
            if num-1 in hash_map:
                dsu.union(idx,hash_map[num-1])
            if num+1 in hash_map:
                dsu.union(idx,hash_map[num+1])
            hash_map[num]=idx
        # print(dsu.parent)
        # print(dsu.rank)
        return max(dsu.rank)
        # nums = set(nums)
        # longest = 0
        # for x in nums:
        #     if x-1 not in nums:
        #         y = x+1
        #         while y in nums:
        #             y+=1
        #         longest=max(longest,y-x)
        # return longest

obj = Solution()
print(obj.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(obj.longestConsecutive([1,2,0,1]))
