class Solution:
    def queensAttacktheKing(self, queens, king):
        ans = []
        queens = {(i, j) for i, j in queens}
        dirs = [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,1),(1,-1),(-1,1)]
        for dx,dy in dirs:
            kx,ky = king
            nx = kx + dx
            ny = ky + dy
            while 0<=nx<8 and 0<=ny<8:
                if (nx,ny) in queens:
                    ans.append((nx,ny))
                    break
                nx+=dx
                ny+=dy     
        return ans

obj = Solution()
print(obj.queensAttacktheKing([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]],[0,0]))