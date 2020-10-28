from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Simple binary search
        # If the grid was 1d then Binary Search would have worked
        # Option 1, convert 2d grid to 1d grid and then search O(m*n + log(m*n)) solution
        # Treat the 2d grid as 1d grid and solve
        # To map 2d grid to 1 grid, we use x*rows+cols to convert the 2d coordinate to 1d
        # Need to do the reverse here
        
        found = False
        rows = len(matrix)
        if not rows:
            return False
        cols = len(matrix[0])
        left = 0
        right = rows*cols - 1
        
        while left<=right:
            pivot = left + (right-left)//2
            pivot_element = matrix[pivot//cols][pivot%cols]
            if pivot_element == target:
                found = True
                break
            elif pivot_element > target:
                right = pivot - 1
            else:
                left = pivot + 1
        return found

tc = [([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3), ([[1,3,5,7],[10,11,16,20],[23,30,34,50]],13)]
obj = Solution()
for arr,target in tc:
    print(obj.searchMatrix(arr,target))