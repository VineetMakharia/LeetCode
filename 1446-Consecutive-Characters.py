class Solution:
    def maxPower(self, s: str) -> int:
        # Sliding window
        if not s:
            return 0
        if len(s)==1:
            return 1
        left = 0
        right = 1
        ans = float('-inf')
        
        while right<len(s):
            curr = s[right]
            prev = s[left]
            # If current and prev are not same, then we need to shrink the window
            if curr!=prev:
                left = right
                continue
            # Keep on increasing the window size otherwise
            ans = max(ans,right-left+1)
            right+=1
            
        return ans

tc = ["leetcode", "abbcccddddeeeeedcba", "triplepillooooow", "cc"]
obj = Solution()
for t in tc:
    print(obj.maxPower(t))