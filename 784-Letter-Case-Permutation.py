class Solution:
    def letterCasePermutation(self, S):
        res = []
        self.dfs(S,'',0,res)
        return res
    
    def dfs(self, og_string, new_string, index, res):
        if len(new_string) == len(og_string):
            res.append(new_string)
        elif og_string[index].isalpha():
            self.dfs(og_string, new_string+og_string[index].upper(), index+1, res)
            self.dfs(og_string, new_string+og_string[index].lower(), index+1, res)
        else:
            self.dfs(og_string, new_string + og_string[index], index+1, res)



obj = Solution()
print(obj.letterCasePermutation("a1b2c"))