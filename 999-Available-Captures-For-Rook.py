class Solution:
    def numRookCaptures(self, board):
        # Basic idea is to move the rook in 4 directions
        rows = len(board)
        cols = len(board[0])
        ans = 0
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(rows):
            for j in range(cols):
                # Rook found
                if board[i][j]=="R":
                    for dx,dy in dirs:
                        nx = i
                        ny = j
                        while 0<=nx<rows and 0<=ny<cols and board[nx][ny]!="B":
                            if board[nx][ny]=="p":
                                ans+=1
                                break
                            nx+=dx
                            ny+=dy
        return ans

obj = Solution()
print(obj.numRookCaptures([ [".",".",".","p",".",".",".","."],
                            [".",".",".","B",".",".",".","."],
                            [".",".",".","R",".",".",".","p"],
                            [".",".",".","B",".",".",".","."],
                            [".",".",".",".",".",".",".","."],
                            [".",".",".","p",".",".",".","."],
                            [".",".",".",".",".",".",".","."],
                            [".",".",".",".",".",".",".","."]]))