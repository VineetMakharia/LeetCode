class Solution:
    def titleToNumber(self, s: str) -> int:
        mapping = {chr(ord('A')+i): (i+1) for i in range(26)}
        # print(mapping)
        col_number = 0
        for char in s:
            col_number = 26*col_number + mapping[char]
        return col_number

obj = Solution()
tc = ["A","AB","ZY"]
for t in tc:
    print(obj.titleToNumber(t))