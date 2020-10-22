class Solution:
    def reverseWords(self, s: str) -> str:
        # Remove all the trailing white spaces
        arr = s.split()
        return " ".join(arr[::-1])

obj = Solution()
print(obj.reverseWords("the sky is blue"))
print(obj.reverseWords("  hello world  "))