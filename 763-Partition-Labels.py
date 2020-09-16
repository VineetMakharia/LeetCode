class Solution:
    def partitionLabels(self, S):
        right = 0
        hash_map = dict()
        left = 0
        for idx,char in enumerate(S):
            hash_map[char]=idx
        # print(hash_map)
        # Hash_map where the last positions of char is saved
        res = []
        for idx, char in enumerate(S):
            right = max(right,hash_map[char])
            if idx == right:
                res.append(right-left+1)
                left=right+1
        return res

obj = Solution()
print(obj.partitionLabels("ababcbacadefegdehijhklij"))