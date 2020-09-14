class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0
        res = [1] * n
        res[0] = res[1] = 0
        for i in range(2, n):
            if res[i] == 1:
                for j in range(2, (n-1)//i+1):
                    res[i*j] = 0
        return sum(res)

obj = Solution()
print(obj.countPrimes(10))