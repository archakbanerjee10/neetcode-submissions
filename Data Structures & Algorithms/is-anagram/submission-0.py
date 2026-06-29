class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
                
        t_dict = {}
        for i in range(len(t)):
            if t[i] in t_dict:
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 1 

        # Shortcut: This will naturally evaluate to True or False!
        return s_dict == t_dict
        