class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Basic idea is to keep track of the brackets that are matching
        # The stack contains all indices of opening brackets
        # If the stack is not empty that means that we need to delete few opening also
        s = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                # If stack is not empty that means that there exists a corresonding opening bracker
                if stack:
                    stack.pop()
                # If the stack is empty that means that this closing needs to be deleted so we mark it as empty character
                else:
                    s[i] = ''
        # Make all the extra opening brackets as empty as well
        while stack:
            x = stack.pop()
            s[x] = ''
        # All the empty will get removed when we use join
        return ''.join(s)

tc = ["lee(t(c)o)de)","a)b(c)d","))((", "(a(b(c)d)"]
obj = Solution()
for t in tc:
    print(obj.minRemoveToMakeValid(t))