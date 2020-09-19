class Solution:
    def maxArea(self, height):
        ans = -1
        left = 0
        right = len(height)-1
        while left<right:
            vertical = min(height[left],height[right])
            horizontal = right-left
            ans = max(ans,horizontal*vertical)
            if height[right]>height[left]:
                left+=1
            else:
                right-=1
        return ans

obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))