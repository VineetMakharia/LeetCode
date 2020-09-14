class Solution:
    def numJewelsInStones(self, J, S):
        setJ = set(J)
        count=0
        for stone in S:
            if stone in setJ:
                count+=1
        return count

obj = Solution()
print(obj.numJewelsInStones("aA","aAAbbbb"))