from typing import List
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        set_deadends = set(deadends)
        initial = "0000"
        from collections import deque
        queue = deque()
        queue.append((initial,0))
        visited = set(initial)
        possible_mappings = {0:[1,9],1:[0,2],2:[1,3],3:[2,4],4:[3,5],5:[4,6],6:[5,7],7:[6,8],8:[7,9],9:[0,8]}
        while queue:
            sz = len(queue)
            for i in range(sz):
                current_state, turns = queue.popleft()
                if current_state in set_deadends:
                    continue
                if current_state == target:
                    return turns
                for i in range(len(current_state)):
                    digit = int(current_state[i])
                    for next_digit in possible_mappings[digit]:
                        new_string = current_state[:i]+str(next_digit)+current_state[i+1:]
                        if new_string not in visited:
                            visited.add(new_string)
                            queue.append((new_string,turns+1))
        return -1

obj = Solution()
print(obj.openLock(["0201","0101","0102","1212","2002"],"0202"))