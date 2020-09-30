class Solution:
    def isValidSudoku(self, arr):
        def notInRow(arr, row):
            st = set()  
            for i in range(9):    
                if arr[row][i] in st:  
                    return False  
                if arr[row][i] != '.':  
                    st.add(arr[row][i])  
            return True
        
        def notInCol(arr, col):  
            st = set()  
            for i in range(9):  
                if arr[i][col] in st: 
                    return False  
                if arr[i][col] != '.':  
                    st.add(arr[i][col])  
            return True
        
        def notInBox(arr, startRow, startCol):  
            st = set()  
            for row in range(3):  
                for col in range(3):  
                    curr = arr[row + startRow][col + startCol]  
                    if curr in st:  
                        return False
                    if curr != '.':  
                        st.add(curr)  
            return True 
        
        def isValid(arr, row, col):  
            return (notInRow(arr, row) and notInCol(arr, col) and
                    notInBox(arr, row - row % 3, col - col % 3))  
        
        for i in range(9):  
            for j in range(9):
                if arr[i][j]!=".":
                    if not isValid(arr, i, j):  
                        return False
        return True

obj = Solution()
print(obj.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))
print(obj.isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))