from typing import List
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = 0
        n = len(s)
        left = 0
        while left<n:
            total_cost = 0  
            max_cost = 0
            right = left
            while right<n and s[right]==s[left]:
                total_cost+=cost[right]
                max_cost = max(max_cost,cost[right])
                right+=1
            ans+=(total_cost-max_cost)
            left = right
        return ans

obj = Solution()
print(obj.minCost("abaac", [1,2,3,4,5]))
            