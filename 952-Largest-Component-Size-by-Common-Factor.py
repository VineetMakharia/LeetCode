# Generic DSU template
# Initialize rank to 1 to find the largest connected component 
from collections import defaultdict
from math import sqrt
class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    # Path compression
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    #Union by rank
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.rank[px]+=self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py]+=self.rank[px]
            
            
class Solution:
    def largestComponentSize(self, A):
        n = len(A)
        dsu = DSU(n)
        primes = defaultdict(list)
        for i, num in enumerate(A):
            # Find all the prime factors of num
            # So, 35 returns {5,7}
            # 4 returns {2}
            pr_set = self.primes_set(num)
            # Now, we need to correctly place them
            # For example - 4,6,15,35,13
            # index = 0, 4 --> {2}
            # index = 1, 6 -->{2,3}
            # index = 2, 15 --> {3,5}
            # index = 3, 35 --> {5,7}
            # index = 4, 13 --> {13}
            for q in pr_set: 
                primes[q].append(i)
            # primes = {2:[0,1], 3: [1,2], 5: [2,3], 7: [3], 13: [4]}
        # Now simply merge everything
        for _, indexes in primes.items():
            for i in range(len(indexes)-1):
                dsu.union(indexes[i], indexes[i+1])
                # union(0,1) --> 0,1
                # union(1,2) --> 0,1,2
                # union (2,3) --> 0,1,2,3
        # Non-optimal way of doing this  
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if self.gcd(A[i],A[j]) > 1:
        #             dsu.union(i,j)
        # print(dsu.rank)
        return max(dsu.rank)
    
    def primes_set(self,n):
        # 35
        # i in range(2,6) --> 2,3,4,5 return func(7) | {5}
        # 7
        # i in range(2,3) --> 3,3 , return {7}
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                # This is equivaluent to return set([i]).union(self.primes_set(n//i))
                return set([i]) | (self.primes_set(n//i))
        return set([n])
    
    def gcd(self,x,y):
        return gcd(y,x%y) if y!=0 else 0

obj = Solution()
print(obj.largestComponentSize([20,50,9,63]))
print(obj.largestComponentSize([4,6,15,35]))
print(obj.largestComponentSize([2,3,6,7,4,12,21,39]))
                
        
        
        