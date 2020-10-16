class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        opening_count = 0
        count = 0
        for char in S:
            if char == '(':
                opening_count+=1
            else:
                if opening_count>0:
                    opening_count-=1
                else:
                    count+=1
        return opening_count + count

test_cases = ["())","(((","()","()))(("]
obj = Solution()
for tc in test_cases:
    print(obj.minAddToMakeValid(tc))