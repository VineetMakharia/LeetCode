class Solution:
    def toLowerCase(self, str):
        arr = []
        for char in str:
            if ord("A") <= ord(char) <= ord("Z"):
                arr.append(chr(ord(char)+32))
            else:
                arr.append(char)
        return "".join(arr)

obj = Solution()
print(obj.toLowerCase("HeLlO"))