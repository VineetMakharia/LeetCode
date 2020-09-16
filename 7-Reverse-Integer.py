class Solution:
    def reverse(self, x):
        is_neg = False
        if (x < 0):
            is_neg = True
            x = x * -1
        temp = str(x)[::-1]
        res = int(temp)
        if (is_neg):
            res = res * -1
        if (abs(res) > (2**31 - 1)):
            return 0
        return res

obj = Solution()
print(obj.reverse(-10111))
print(obj.reverse(10111))