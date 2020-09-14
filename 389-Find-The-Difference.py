class Solution:
    def findTheDifference(self, s, t):
        # Basic idea is to use XOR
        xored = 0
        for x in (s+t):
            xored^=ord(x)
        return chr(xored)

obj = Solution()
print(obj.findTheDifference("abcd","abced"))