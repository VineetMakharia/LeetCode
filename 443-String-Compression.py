from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 0
        while right < len(chars):
            # while the chars are same, keep on increasing the window size
            if chars[left] == chars[right]:
                right+=1
                continue
            # if window size = 1, then there is only 1 single type of character \
            # thus, we do not add a count of it to after it 
            if right-left==1:
                left = right
            else:
                # Need to remove all the characters after the first occurence and \
                # replace it with the count of it
                # Now there can be 10 characters in a row, thus we need to use len() since \
                # 10 is "1" "0" so 2 different characters
                chars[left+1:right] = str(right-left)
                # Now we need to move the left pointer to the next unique character
                # This can be done by incrementing by one and the len of the new number characters
                left = left + 1 + len(str(right-left))
                # right was pointing to the next new character but we updated our array \
                # so we need to reset the index to the next unique character
                right = left
        return "".join(chars)

obj = Solution()

print(obj.compress(list("aaaabbbbcccccd")))
    