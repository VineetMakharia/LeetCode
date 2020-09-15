class Solution(object):
    def groupAnagrams(self, strs):
        from collections import defaultdict
        hash_map = defaultdict(list)
        for s in strs:
            # sorted_chars = sorted(s)
            # hash_map[tuple(sorted_chars)].append(s)
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            hash_map[tuple(count)].append(s)
        return list(hash_map.values())

res = Solution()
print(res.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))