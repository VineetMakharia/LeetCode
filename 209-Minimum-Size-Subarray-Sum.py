class Solution:
    def minSubArrayLen(self, s, nums):
        ans = float('INF')
        left = 0
        current_sum=0
        threshold = s
        # [2,3,1,2,4,3]
        for i in range(len(nums)):
            current_sum+=nums[i]
            if current_sum < threshold:
                continue
            else:
                while current_sum>=threshold:
                    ans = min(ans, i-left+1)
                    current_sum-=nums[left]
                    left+=1
        return ans if ans!=float('INF') else 0

obj = Solution()
print(obj.minSubArrayLen(7,[2,3,1,2,4,3]))