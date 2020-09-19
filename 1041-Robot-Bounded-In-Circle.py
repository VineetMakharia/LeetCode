class Solution:
    def isRobotBounded(self, instructions):
        x = 0
        y = 0
        # direction: {0: North, 1: East, 2: South, 3:West}
        direction = 0
        for move in instructions:
            # Right--> Add 1 to the directions
            # Adding 4 is not needed in this case, since +ve
            if move == 'R': 
                direction = (4 + direction + 1)%4
            # Left --> Remove -1 from the directions
            # Adding 4 to it, to avoid negative cases, like "LL"
            # Adding 4 to it won't change the direction
            elif move == 'L': 
                direction = (4 + direction - 1)%4
            else:    # if move == 'G'
                if direction == 0: 
                    y += 1
                elif direction == 1: 
                    x += 1
                elif direction == 2: 
                    y -= 1
                else: 
                    x -= 1

        return (x == 0 and y == 0) or direction!=0

obj = Solution()
print(obj.isRobotBounded("GGLLGG"))
print(obj.isRobotBounded("GG"))