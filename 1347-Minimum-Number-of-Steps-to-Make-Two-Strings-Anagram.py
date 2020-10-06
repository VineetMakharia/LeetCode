class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # leetcode = {l:1, e:3, t:1, c:1, o:1, d:1 }
        # practice = {p:1, r:1, a:1, c:2, t:1, i:1, e:1}
        # h1 = [0]*26
        # h2 = [0]*26
        # for char in s:
        #     h1[ord(char)-ord('a')]+=1
        # for char in t:
        #     h2[ord(char)-ord('a')]+=1
        # # print(h1)
        # # print(h2)
        # ans = 0
        # for char in string.ascii_lowercase:
        #     temp = h1[ord(char)-ord('a')] - h2[ord(char)-ord('a')]
        #     ans+=max(0,temp)
        # return ans
            
        from collections import defaultdict, Counter
        # h1 = defaultdict(int)
        # h2 = defaultdict(int)
        # for char in s:
        #     h1[char]+=1
        # for char in t:
        #     h2[char]+=1
        h1 = Counter(s)
        h2 = Counter(t)
        ans = 0
        # print(h1,h2)
        for char in h1:
            ans += max(0,(h1[char] - h2[char]))
        return ans

obj = Solution()
print(obj.minSteps("leetcode","practice"))