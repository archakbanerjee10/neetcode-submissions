class Solution:
    def minWindow(self, s: str, t: str) -> str:

        mydict_t = {}
        for char in t:
            mydict_t[char] = mydict_t.get(char, 0) + 1       
        length = len(mydict_t) # Number of unique characters needed
        have = 0
        left = 0
        ans_len = float("inf") 
        result = ""
        mydict_s = {}
        
        for right in range(len(s)):
            char_in = s[right]
            mydict_s[char_in] = mydict_s.get(char_in, 0) + 1
            
            # Fix 1: Only increment 'have' when exact target frequency is met
            if char_in in mydict_t and mydict_s[char_in] == mydict_t[char_in]:
                have += 1
            
            # Shrink the accordion while it's valid
            while have == length:
                # Fix 3: Update both ans_len and result
                if (right - left + 1) < ans_len:
                    ans_len = right - left + 1
                    result = s[left:right+1]
                
                # Fix 2: Explicitly decrement mydict_s count before checking validity
                char_out = s[left]
                mydict_s[char_out] -= 1
                
                if char_out in mydict_t and mydict_s[char_out] < mydict_t[char_out]:
                    have -= 1
                    
                left += 1
                
        return result
                
            
            


        