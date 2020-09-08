class Solution:
	def repsubs(self,s):
		if len(s)==0:
			return True
		new_str = (s + s)[1:-1]
		return s in new_str


obj = Solution()
print(obj.repsubs("abab"))
print(obj.repsubs("aba"))
print(obj.repsubs("abcabcabcabc"))