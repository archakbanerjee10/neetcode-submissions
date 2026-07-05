class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If we see a duplicate, shrink the window from the left
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            
            # Now it's safe to add the current character
            my_set.add(s[right])
            
            # Update your maximum length dynamically!
            max_length = max(max_length, right - left + 1)
            
        return max_length


        