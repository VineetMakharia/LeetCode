class Solution:
    def isPalindrome(self, s):
        new_string =""
        for x in s:
            if x.isalpha() or x.isdigit():
                new_string += x
        new_string = new_string.lower()
        return new_string==new_string[::-1]

obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))