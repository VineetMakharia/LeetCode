class Solution:
    def lengthOfLastWord(self, s):
        return 0 if not s.split() else len(s.split()[-1])
#         size = 0
#         char_seen = False
#         for i in range(len(s)-1,-1,-1):
#             if not s[i].isalpha():
#                 if char_seen:
#                     break
#                 continue
#             else:
#                 size+=1
#                 char_seen = True
#         return size

obj = Solution()
print(obj.lengthOfLastWord("Hello World"))
print(obj.lengthOfLastWord("  "))
print(obj.lengthOfLastWord(" World "))
            