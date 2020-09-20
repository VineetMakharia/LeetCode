class Solution:
    def sequentialDigits(self, low, high):
        # low = 100
        # high = 300
        from collections import deque
        queue = deque()
        for i in range(1,10):
            queue.append(i)
        # queue = [1,2,3,4,5,6,7,8,9]
        ans = []
        while queue:
            current = queue.popleft()
            # queue = [2...9]
            # current = 1
            # if we're in bounds
            if low<=current<=high:
                ans.append(current)
            # Important condition as loop will never end otherwise
            if current > high:
                break
            # unit = 1
            unit = current%10
            if (unit < 9):
                queue.append(current*10 + (unit+1))
                # queue  = [2..9, 12]
        return sorted(ans)

obj = Solution()
print(obj.sequentialDigits(100,300))