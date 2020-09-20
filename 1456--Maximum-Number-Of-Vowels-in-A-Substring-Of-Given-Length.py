class Solution:
    def maxVowels(self, s, k):
        vowels = set(('a','e','i','o','u'))
        left = 0
        count_of_vowels = 0
        ans = -1
        for idx,char in enumerate(s):
            if idx<k:
                count_of_vowels+=s[idx] in vowels
            else:
                left_char = s[left] in vowels
                right_char = s[idx] in vowels
                count_of_vowels = count_of_vowels - left_char + right_char
                left+=1
            ans = max(ans,count_of_vowels)
        return ans

obj = Solution()
print(obj.maxVowels("abciiidef", 3))
print(obj.maxVowels("rhythms", 4))
                