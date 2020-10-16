class Solution:
    def generate(self, string):
        arr = set()
        from collections import deque
        queue = deque()
        queue.append(list(string))
        while queue:
            # print(queue)
            current_string = queue.popleft()
            found = False
            for i in range(len(current_string)):
                if current_string[i] == "?":
                    found = True
                    current_string[i] = "1"
                    queue.append(current_string[:])
                    current_string[i] = "0"
                    queue.append(current_string[:])
            if not found:
                arr.add("".join(current_string))     
        # def helper(substring,idx,arr,needed_len):
            # if idx == needed_len:
            #     arr.append("".join(substring))
            #     return
            # if substring[idx] == "?":
            #     substring[idx] = "0"
            #     helper(substring,idx+1,arr,needed_len)
            #     substring[idx] = "1"
            #     helper(substring,idx+1,arr,needed_len)
            #     substring[idx] = "?"
            # else:
            #     helper(substring,idx+1,arr,needed_len)
        # helper(list(string),0,arr,len(string))
        return arr


obj = Solution()
print(obj.generate("??"))