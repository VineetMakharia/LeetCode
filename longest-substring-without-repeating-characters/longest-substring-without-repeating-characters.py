class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_window_size = 0
        left = 0
        right = 0
        
        seen = dict()
        
        while right < len(s):
            char_end = s[right]
            if char_end not in seen:
                max_window_size = max(max_window_size, right-left+1)
            else:
                if seen[char_end] < left:   
                    max_window_size = max(max_window_size, right-left+1)
                else:
                    left = seen[char_end]+1
            
            seen[char_end] = right
            right+=1
        
