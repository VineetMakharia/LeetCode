from typing import List
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows = len(board)
        cols = len(board[0])
        remaining_to_crush = False
        
        # 1st idea is to use a representative element like * for marking the candies that need to be crushed but that will fail for the L case
        # Finding all the similar candies in a row
        for i in range(rows):
            for j in range(cols-2):
                if abs(board[i][j])==abs(board[i][j+1])==abs(board[i][j+2])!=0:
                    board[i][j]=-1*abs(board[i][j])
                    board[i][j+1]=-1*abs(board[i][j])
                    board[i][j+2]=-1*abs(board[i][j])
                    remaining_to_crush = True
        
        # Finding all the similar candies in a col
        for i in range(rows-2):
            for j in range(cols):
                if abs(board[i][j])==abs(board[i+1][j])==abs(board[i+2][j])!=0:
                    board[i][j]=-1*abs(board[i][j])
                    board[i+1][j]=-1*abs(board[i][j])
                    board[i+2][j]=-1*abs(board[i][j])
                    remaining_to_crush = True
        
        # Found all the candies that need to be crushed, now use gravity, so iterate through every col
        
        for j in range(cols):
            zeroes = rows-1
            for i in range(rows-1,-1,-1):
                if board[i][j]>0:
                    board[zeroes][j] = board[i][j]
                    zeroes-=1
            
            for x in range(zeroes,-1,-1):
                board[x][j]=0
            
        
        return self.candyCrush(board) if remaining_to_crush else board

obj = Solution()
print(obj.candyCrush([[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]))
            
            
        
        
        
        
        
        
        