class Solution:
    def __init__(self):
        self.res=0
    def totalNQueens(self, n):
        def backtrack(i):
            if i == n:
                self.res+=1
            for j in range(n):
                if j not in cols and i+j not in diag and i-j not in off_diag:
                    cols.add(j)
                    diag.add(i+j)
                    off_diag.add(i-j)
                    board.append("."*(j)+"Q"+"."*(n-j-1))
                    backtrack(i+1)
                    board.pop()
                    off_diag.remove(i-j)
                    diag.remove(i+j)
                    cols.remove(j)
        board = []
        cols = set()
        diag = set()
        off_diag = set()
        backtrack(0)
        return self.res

obj = Solution()
print(obj.totalNQueens(4))