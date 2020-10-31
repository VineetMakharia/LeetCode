from typing import List
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        ranks = len(votes[0])
        # Basic idea is to build a hashmap to record the number of votes for every character
        # Need to add the character to the end, since in case of a tie we need to alphabetically rank them
        hash_map = {char : [0]*ranks + [char] for char in votes[0]}
        # Decrement rank over here, since you need the highest rank 
        for ranking in votes:
            for idx,char in enumerate(ranking):
                hash_map[char][idx]-=1
        # Our hash_map now has char:list and we simply just need to sort the values
        arr = sorted(hash_map.values())
        # Now that we have sorted it, we can just use the last char of the element
        return "".join([ele[-1] for ele in arr])


obj = Solution()
tc = [["ABC","ACB","ABC","ACB","ACB"], ["WXYZ","XYZW"]]
for t in tc:
    print(obj.rankTeams(t))