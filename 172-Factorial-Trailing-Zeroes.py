class Solution:
    def trailingZeroes(self, n):
        count = 0
        while n > 0:
            n = n / 5
            count = count + n
        return count

obj = Solution()
print(obj.trailingZeroes(10))