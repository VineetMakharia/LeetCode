class Solution:
    def solveNQueens(self, n):
        def backtrack(i):
            if i == n:
                res.append(list(board))
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
        res = []
        board = []
        cols = set()
        diag = set()
        off_diag = set()
        backtrack(0)
        return res

obj = Solution()
print(obj.solveNQueens(4))