class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Build a stack of char * freq (can't use tuples because they are immutable)
        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        
        return "".join(char*count for char,count in stack)

tc = [["abcd",2], ["deeedbbcccbdaa",3], ["pbbcggttciiippooaais", 2]]
obj = Solution()
for t in tc:
    print(obj.removeDuplicates(*t))
                    