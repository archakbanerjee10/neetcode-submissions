class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict={}
        left=0
        max_length=0
        for right in range(len(s)):
            char_in=s[right]
            my_dict[char_in] = my_dict.get(char_in, 0) + 1
            max_freq = max(my_dict.values())
            win_len = right - left + 1
            if(win_len-max_freq)>k:
                char_out=s[left]
                my_dict[char_out]-=1
                left+=1
            max_length=max(max_length,right-left+1)
        return max_length
            


        