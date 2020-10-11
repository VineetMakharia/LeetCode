# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass

class Solution:
    def findCelebrity(self, n: int) -> int:
        stack = []
        for i in range(n):
            stack.append(i)
        
        while len(stack)>1:
            a = stack.pop()
            b = stack.pop()
            if knows(a,b):
                stack.append(b)
            else:
                stack.append(a)
        
        candidate = stack.pop()
        
        for i in range(n):
            if (knows(candidate,i) and candidate!=i) or not knows(i,candidate):
                return -1
        return candidate
            