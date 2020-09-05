class Solution:
    def letterCombinations(self, digits):
        mapping = {'2':'abc',
                  '3':'def',
                  '4':'ghi',
                  '5':'jkl',
                  '6':'mno',
                  '7':'pqrs',
                  '8':'tuv',
                  '9':'wxyz'}
        res = []
        self.dfs(digits,mapping,res,"",len(digits))
        return res

    def dfs(self,digits,mapping,res,current,req_size):
    	if len(current) == req_size:
    		res.append(current)
    		return
    	current_digit = digits[0]
    	for char in mapping[current_digit]:
    		self.dfs(digits[1:],mapping,res,current+char,req_size)

obj = Solution()
print(obj.letterCombinations("23"))
print(obj.letterCombinations("79"))