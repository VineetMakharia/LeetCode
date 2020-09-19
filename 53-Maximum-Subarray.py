class Solution:
    def maxSubArray(self, A):
        if not A:
            return 0
        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum
obj = Solution()
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))